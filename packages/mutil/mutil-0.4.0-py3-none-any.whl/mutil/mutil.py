#!/usr/bin/env python3
#===============================================================================
# mutil.py
#===============================================================================

"""Utilities for managing the memory policy"""




# Imports ======================================================================

import json
import os
import psutil
import subprocess
from argparse import ArgumentParser
from mutil.version import __version__
import sys
import shutil
import getpass
import itertools





# Globals ======================================================================

PROPOSED_POLICY_PATH = '/home/memory-policy/proposed-memory-policy.json'
CURRENT_POLICY_PATH =  '/home/memory-policy/current-memory-policy.json'
PREVIOUS_POLICY_PATH =  '/home/memory-policy/previous-memory-policy.json'

CGCONFIG_BASE = ''
CGCONFIG_PATH = '/etc/cgconfig.conf'
CGRULES_PATH = '/etc/cgrules.conf'
CGRULES_BASE  = '\t'.join(('#<user/group>', '<controller(s)>', '<cgroup>'))
MEMORY_CUSHION_GB = 8




# Functions ====================================================================

def require_super_user():
    """Check that the current command is being run with superuser privileges
    
    Raise an exception if it is not.
    """
    
    if not os.geteuid() == 0:
        raise SystemExit('Superuser required')


def load_policy(policy_path):
    """Load a memory policy (JSON file) from disk
    
    Parameters
    ----------
    policy_path : str
        Path to the memory policy file
    
    Returns
    -------
    dict
        Dictionary defining a memory policy
    """
    
    with open(policy_path, 'r') as f:
        policy = json.load(f)
    return policy


def get_usage_for_a_user(user):
    """Get estimated memory usage for a user
    
    Parameters
    ----------
    user : str
        User to retrieve
    
    Returns
    -------
    int
        Estimated memory usage in bytes
    """

    with subprocess.Popen(
        ('ps', '-U', user, '--no-headers', '-o', 'rss'),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    ) as ps:
        with subprocess.Popen(
            ('awk', '{ sum+=$1} END {print sum}'),
            stdin=ps.stdout,
            stdout=subprocess.PIPE
        ) as awk:
            usage_bytes, _ = awk.communicate()
            usage_str = usage_bytes.decode().rstrip('\n')
            return int(usage_str) if usage_str else 0


def convert_usage(usage, kilobytes=False, megabytes=False):
    """Convert units of memory

    Converts to gigabytes unless the `kilobytes` or `megabytes` argument is
    given.
    
    Parameters
    ----------
    usage : int
        Memory usage in bytes
    kilobytes : bool
        Convert to kilobytes
    megabytes : bool
        Convert to megabytes
    
    Returns
    -------
    int
        Converted value
    """

    return int(usage / (1024 ** (2 - (2 * kilobytes) - (1 * megabytes))))


def print_shared(shared_memory, comma=False):
    """Print the shared memory value
    
    Parameters
    ----------
    memory_limit_gb : int
        Overall memory limit in gigabytes
    shared_memory : int
        Shared memory usage in gigabytes
    """

    print('  "shared": {}{}'.format(shared_memory, ',' * comma))


def print_group(
    group_name,
    group,
    comma=False
):
    """Print the shared memory value
    
    Parameters
    ----------
    memory_limit_gb : int
        Overall memory limit in gigabytes
    shared_memory : int
        Shared memory usage in gigabytes
    """

    group_usage = convert_usage(
        sum(get_usage_for_a_user(user) for user in group['users'])
    )
    print('  "{}"'.format(group_name))
    print(': {')
    lines = json.dumps(group, indent=2, sort_keys=True).splitlines()[1:]
    for line in lines:
        if line.strip(' :",') in group['users']:
            print('  {}'.format(line.rstrip(',')))
            print(',')
        else:
            print('  {}{}'.format(line, ',' * (line == '}' and comma)))
    


def print_policy(policy):
    """Print a memory policy (JSON file) to standard output
    
    Parameters
    ----------
    policy : dict
        Dictionary defining the policy
    """

    print(json.dumps(policy, indent=2, sort_keys=True))


def dump_policy(policy, policy_path):
    """Write a memory policy (JSON file) to disk
    
    Parameters
    ----------
    policy : dict
        Dictionary defining the policy
    policy_path : str
        Path to write the memory policy file
    """
    
    with open(policy_path, 'w') as f:
        json.dump(policy, f)


def get_group_set(policy):
    """Get the set of group names in a policy
    
    Parameters
    ----------
    policy : dict
        Dictionary defining the policy
    
    Returns
    -------
    set
        The group names in the policy
    """
    
    return set(policy.keys()) - {'shared'}


def get_user_set(policy):
    """Get the set of users in a policy
    
    Parameters
    ----------
    policy : dict
        Dictionary defining the policy
    
    Returns
    -------
    set
        The users in the policy
    """
    
    return set(
        user
        for group in get_group_set(policy)
        for user in policy[group]['users']
)


def validate_user(user, users):
    """Check if a user is contained in the indicated group of users
    
    Raise an exception if not.
    
    Parameters
    ----------
    user : str
        User to validate
    users : container
        Container of valid users
    """
    if user not in users:
        raise Exception(
            "It looks like you're trying to free memory before being inducted "
            'into the policy. Use "minduct" to induct yourself before'
            ' continuing.'
        )


def validate_group(group_name):
    """Check that a group of users is not named ``free`` or ``shared``
    
    Parameters
    ----------
    group_name : str
        Group name to be validated
    """
    
    if group_name == 'free':
        raise Exception(
            'Can\'t free memory from the "free" group... it\'s already free.'
        )
    elif group_name == 'shared':
        raise Exception('"shared" can\'t be a group name')


def specified_users(users_arg, users):
    """Parse a comma-separated list of users
    
    Check that all specified users are valid, and return them as a list
    
    Parameters
    ----------
    users_arg : str
        Comma-separated list of users
    users : container
        Container of valid users
    
    Returns
    -------
    list
        List of specified users
    """
    if set(users_arg.split(',')) <= users:
        users = users_arg.split(',')
        return users
    else:
        raise Exception(
            'Some of the specified users have not yet been inducted into the '
            'policy. Use minduct -u to induct them before continuing.'
        )


def remove_user_from_current_group(user, policy):
    """Remove a user from a group they are currently a member of
    
    Parameters
    ----------
    user : str
        User to remove
    policy : dict
        Policy to modify
    """
    
    for group in get_group_set(policy):
        if user in policy[group]['users']:
            if (policy[group]['users'] == [user]) and (group != 'free'):
                del policy[group]
            else:
                policy[group]['users'].remove(user)
            break


def free_gigabytes():
    """Wraps the unix command `free -g`
    
    Returns
    -------
    tuple
        total, used, free, shared, buff_cache, available
    """
    
    with subprocess.Popen(('free', '-g'), stdout=subprocess.PIPE) as proc:
        return (
            int(val) for val in
            proc.communicate()[0].decode().splitlines()[1].split()[1:]
        )


def memory_limit_in_gigabytes():
    """Calculate the memory limit in gigabytes
    
    Returns
    -------
    int
        The memory limit (in gigabytes)
    """
    
    _, used, _, _, _, available = free_gigabytes()
    return used + available - MEMORY_CUSHION_GB
#     return math.floor(
#         (psutil.virtual_memory().available + psutil.virtual_memory().used)
#         / 2**30
#     )


def shared_memory_in_gigabytes():
    """Look up the shared memory in gigabytes
    
    Returns
    -------
    int
        The shared memory (in gigabytes)
    """
    
    _, _, _, shared, _, _ = free_gigabytes()
    return shared
#     return math.floor(psutil.virtual_memory().shared / 2**30)


def available_memory(policy):
    """Calculate the available memory in gigabytes
    
    Returns
    -------
    int
        The available memory (in gigabytes)
    """
    
    limit = memory_limit_in_gigabytes()
    available_memory_in_gigabytes = (
        limit - sum(
            policy[group]['memory_limit']
            for group in get_group_set(policy) - {'free'}
        )
    )
    if available_memory_in_gigabytes < 16:
        raise Exception(
            'This action would bring the total reserved memory above {}G, '
            'which is not allowed. Please reserve less.'
            .format(limit - 16)
        )
    else:
        return available_memory_in_gigabytes


def reserved_memory(policy):
    """Calculate the amount of reserved memory according to the given policy
    
    Returns
    -------
    int
        The reserved memory (in gigabytes)
    """
    return sum(
        policy[group]['memory_limit']
        for group in get_group_set(policy) - {'free'})


def validate_draft_policy(
    draft,
    total_reserved_memory,
    draft_users,
    proposed_policy_users
):
    """Check that a draft policy is valid, and raise an exception if not
    
    Parameters
    ----------
    draft : dict
        Dictionary defining the draft policy
    total_reserved_memory : int
        The total memory reserved by the draft policy in gigabytes
    draft_users : set
        The users present in the draft
    proposed_policy_users : set
        The users present in the extant proposed policy
    """
    
    if {'free', 'shared'} < set(draft.keys()):
        raise Exception(
            '"free" and "shared" are reserved words and should not be group '
            'names in a policy draft.'
        )
    limit = memory_limit_in_gigabytes()
    if total_reserved_memory >= (limit - 16):
        raise Exception(
            'This draft reserves more than {}G of memory, please reserve '
            'less.'
            .format(limit - 16)
        )
    for user in draft_users:
        if user not in proposed_policy_users:
            raise Exception(
                'Induct new users before drafting a policy that includes them'
            )


def infer_free_group(
    draft,
    total_reserved_memory,
    draft_users,
    proposed_policy_users
):
    """Infer the free group for a draft policy
    
    Parameters
    ----------
    draft : dict
        Dictionary defining the draft policy
    total_reserved_memory : int
        The total memory reserved by the draft policy in gigabytes
    draft_users : set
        The users present in the draft
    proposed_policy_users : set
        The users present in the extant proposed policy
    
    Returns
    -------
    dict
        The "free" group to fill out a memory policy
    """
    
    return {
        'memory_limit': memory_limit_in_gigabytes() - total_reserved_memory,
        'users': list(proposed_policy_users - draft_users)
    }


def generate_config_files(policy):
    """Generate config files for cgroups
    
    Parameters
    ----------
    policy : dict
        Dictionary defining a memory policy
    
    Returns
    -------
    str, str
        Tuple of two strings: the cgconfig and cgrules files, respectively.
    """
    
    cgconfig_list = [CGCONFIG_BASE]
    cgrules_list = [CGRULES_BASE]
    for group in get_group_set(policy):
        cgconfig_list.append(
                (
'''group {0} {{
    memory {{
        memory.limit_in_bytes="{1}G";
        memory.swappiness=0;
    }}
}}

'''
                ).format(group, policy[group]['memory_limit'])
            )
        for user in policy[group]['users']:
            cgrules_list.append('\t'.join((user, 'memory', group)))
    return ''.join(cgconfig_list), '\n'.join(cgrules_list) + '\n'


def restart_daemons():
    """Restart the cgroups daemons (putting a configuration into effect)"""
    
    for proc in psutil.process_iter():
        if proc.name() == 'cgrulesengd':
            proc.kill()
    subprocess.call(('cgconfigparser', '-l', '/etc/cgconfig.conf'))
    subprocess.call(('cgrulesengd'))


def enact_policy(policy, no_daemon=False):
    """Enact a memory policy by writing new cgroup config files
    
    Restart the daemons if required
    
    Parameters
    ----------
    policy : dict
        Memory policy to enact
    no_daemon : bool
        If True, don't restart the cgroup daemons
    """
    
    cgconfig, cgrules = generate_config_files(policy)
    with open(CGCONFIG_PATH, 'w') as f:
        f.write(cgconfig)
    with open(CGRULES_PATH, 'w') as f:
        f.write(cgrules)
    if no_daemon:
        subprocess.call(('cgconfigparser', '-l', '/etc/cgconfig.conf'))
    else:
        restart_daemons()


def load_draft(arg):
    try:
        draft = json.loads(arg)
    except:
        with open(arg, 'r') as f:
            draft = json.load(f)
    return draft


def validate_memory_quantity(memory_in_gigabytes):
    if memory_in_gigabytes < 1:
        raise Exception(
            'It doesn\'t make sense to make a reservation with < 1G memory. Use '
            'mfree if you need to free up some memory.'
        )


def remove_users_from_current_groups(users, policy):
    for user in users:
        remove_user_from_current_group(user, policy)


def reserve(memory_in_gigabytes, group, users, policy):
    policy[group] = {'memory_limit': memory_in_gigabytes, 'users': users}


def mcurrent(args):
    policy = load_policy(CURRENT_POLICY_PATH)
    print_policy(policy)


def mprevious(args):
    policy = load_policy(PREVIOUS_POLICY_PATH)
    print_policy(policy)


def mproposed(args):
    policy = load_policy(PROPOSED_POLICY_PATH)
    print_policy(policy)


def mdraft(args):
    draft = load_draft(args.draft)
    draft_users = get_user_set(draft)
    total_reserved_memory = reserved_memory(draft)
    proposed_policy = load_policy(PROPOSED_POLICY_PATH)
    proposed_policy_users = get_user_set(proposed_policy)
    validate_draft_policy(
        draft, total_reserved_memory, draft_users, proposed_policy_users)
    draft['free'] = infer_free_group(
        draft, total_reserved_memory, draft_users, proposed_policy_users)
    draft['shared'] = shared_memory_in_gigabytes()
    dump_policy(draft, PROPOSED_POLICY_PATH)


def menact(args):
    require_super_user()
    shutil.move(CURRENT_POLICY_PATH, PREVIOUS_POLICY_PATH)
    shutil.copy(PROPOSED_POLICY_PATH, CURRENT_POLICY_PATH)
    policy = load_policy(CURRENT_POLICY_PATH)
    enact_policy(policy, no_daemon=args.no_daemon)


def mfree(args):
    validate_group(args.group)
    policy = load_policy(PROPOSED_POLICY_PATH)
    user = getpass.getuser()
    users = get_user_set(policy)
    validate_user(user, users)
    if not (args.group or args.users):
        if user in policy['free']['users']:
            raise Exception('You have no reserved memory to free.')
        remove_user_from_current_group(user, policy)
        policy['free']['users'].append(user)
    elif args.group and (not args.users):
        try:
            for user in policy[args.group]['users']:
                policy['free']['users'].append(user)
            del policy[args.group]
        except KeyError:
            raise Exception('The specified group does not exist.')
    elif (not args.group) and args.users:
        users = specified_users(args.users, users)
        for user in users:
            remove_user_from_current_group(user, policy)
            policy['free']['users'].append(user)
    elif args.group and args.users:
        users = specified_users(args.users, users)
        for user in users:
            remove_user_from_current_group(user, policy)
            policy['free']['users'].append(user)
    policy['free']['memory_limit'] = available_memory(policy)
    policy['shared'] = shared_memory_in_gigabytes()
    dump_policy(policy, PROPOSED_POLICY_PATH)


def minduct(args):
    new_users = set(user for user in args.users.split(','))
    policy = load_policy(PROPOSED_POLICY_PATH)
    existing_users = get_user_set(policy)
    for user in new_users.intersection(existing_users):
        print('{} is already in the memory policy.'.format(user))
    policy['free']['users'].extend(list(new_users - existing_users))
    dump_policy(policy, PROPOSED_POLICY_PATH)
    for user in new_users - existing_users:
        print('{} has been inducted into the memory policy.'.format(user))


def mrepeal(args):
    require_super_user()
    shutil.copy(PREVIOUS_POLICY_PATH, CURRENT_POLICY_PATH)
    policy = load_policy(CURRENT_POLICY_PATH)
    cgconfig, cgrules = generate_config_files(policy)
    with open(CGCONFIG_PATH, 'w') as f:
        f.write(cgconfig)
    with open(CGRULES_PATH, 'w') as f:
        f.write(cgrules)
    restart_daemons()


def mreserve(args):
    validate_memory_quantity(args.memory_in_gigabytes)
    validate_group(args.group)
    policy = load_policy(PROPOSED_POLICY_PATH)
    user = getpass.getuser()
    users = get_user_set(policy)
    validate_user(user, users)
    if (
        (args.group in users) and
        (args.group not in (args.users.split(',') if args.users else {user}))
    ):
        raise Exception(
            'Better not use a username as a group name unless that user is in '
            'the group.'
        )
    if not (args.group or args.users):
        if user in policy['free']['users']:
            reserve(args.memory_in_gigabytes, user, [user], policy)
            policy['free']['users'].remove(user)
        else:
            for group in (get_group_set(policy) - {'free'}):
                if user in policy[group]['users']:
                    policy[group]['memory_limit'] = args.memory_in_gigabytes
                    break
    elif args.group and (not args.users):
        try:
            policy[args.group]['memory_limit'] = args.memory_in_gigabytes
        except KeyError:
            remove_users_from_current_groups([user], policy)
            reserve(args.memory_in_gigabytes, args.group, [user], policy)
    elif (not args.group) and args.users:
        users = specified_users(args.users, users)
        group = '_'.join(users)
        try:
            policy[group]['memory_limit'] = args.memory_in_gigabytes
        except KeyError:
            remove_users_from_current_groups(users, policy)
            reserve(args.memory_in_gigabytes, group, users, policy)
    elif args.group and args.users:
        users = specified_users(args.users, users)
        try:
            for user in set(policy[args.group]['users']) - set(users):
                policy[args.group]['users'].remove(user)
                policy['free']['users'].append(user)
            for user in set(users) - set(policy[args.group]['users']):
                remove_user_from_current_group(user, policy)
                policy[args.group]['users'].append(user)
        except KeyError:
            remove_users_from_current_groups(users, policy)
            reserve(args.memory_in_gigabytes, args.group, users, policy)
    policy['free']['memory_limit'] = available_memory(policy)
    dump_policy(policy, PROPOSED_POLICY_PATH)


def mretire(args):
    users_to_retire = set(user for user in args.users.split(','))
    if getpass.getuser() in users_to_retire:
        raise Exception("You can't retire yourself")
    policy = load_policy(PROPOSED_POLICY_PATH)
    existing_users = get_user_set(policy)
    for user in users_to_retire - existing_users:
        print('{} is not in the memory policy.'.format(user))
    for user in users_to_retire.intersection(existing_users):
        remove_user_from_current_group(user, policy)
        print('{} has been retired from the memory policy.'.format(user))
    dump_policy(policy, PROPOSED_POLICY_PATH)


def stringify_usage(converted_usage, kilobytes=False, megabytes=False):
    return '{}{}'.format(converted_usage,
        ('K' * kilobytes + 'M' * megabytes) if kilobytes or megabytes
        else 'G')


def display_usage_for_a_user(user, kilobytes=False, megabytes=False):
    usage = get_usage_for_a_user(user)
    print('{}: {}'.format(user, stringify_usage(convert_usage(
                    usage, kilobytes=kilobytes, megabytes=megabytes
                ), kilobytes=kilobytes, megabytes=megabytes)))


def display_usage_for_a_group(policy, group, kilobytes=False, megabytes=False):
    group_usage = sum(get_usage_for_a_user(user)
        for user in policy[group]['users'])
    print('{}: {}'.format(group, stringify_usage(convert_usage(
                    group_usage, kilobytes=kilobytes, megabytes=megabytes
                ), kilobytes=kilobytes, megabytes=megabytes)))
    for user in policy[group]['users']:
        usage = get_usage_for_a_user(user)
        print('  {}: {}'.format(user, stringify_usage(convert_usage(
                        usage, kilobytes=kilobytes, megabytes=megabytes),
                    kilobytes=kilobytes, megabytes=megabytes)))


def display_total_usage_for_users(users, kilobytes=False, megabytes=False):
    total_usage = sum(get_usage_for_a_user(user) for user in users)
    print('{}: {}'.format('TOTAL', stringify_usage(convert_usage(
        total_usage, kilobytes=kilobytes, megabytes=megabytes),
            kilobytes=kilobytes, megabytes=megabytes)))


def musage(args):
    if not (args.groups or args.users):
        display_usage_for_a_user(getpass.getuser(), kilobytes=args.kilobytes,
                                 megabytes=args.megabytes)
    elif args.groups and (not args.users):
        groups = args.groups.split(',')
        policy = load_policy(CURRENT_POLICY_PATH)
        if set(groups) - set(policy.keys()):
            raise Exception('group(s) {} not present in the policy'.format(
                ', '.join(set(groups) - set(policy.keys()))))
        users = {user for group in groups for user in policy[group]['users']}
        for group in groups:
            display_usage_for_a_group(policy, group, kilobytes=args.kilobytes,
                                      megabytes=args.megabytes)
        if len(groups) > 1:
            display_total_usage_for_users(users, kilobytes=args.kilobytes,
                                          megabytes=args.megabytes)
    elif (not args.groups) and args.users:
        users = set(user for user in args.users.split(','))
        for user in users:
            display_usage_for_a_user(user, kilobytes=args.kilobytes,
                                     megabytes=args.megabytes)
        if len(users) > 1:
            display_total_usage_for_users(users, kilobytes=args.kilobytes,
                                          megabytes=args.megabytes)
    elif args.groups and args.users:
        groups = args.groups.split(',')
        users = set(user for user in args.users.split(','))
        policy = load_policy(CURRENT_POLICY_PATH)
        if set(groups) - set(policy.keys()):
            raise Exception('group(s) {} not present in the policy'.format(
                ', '.join(set(groups) - set(policy.keys()))))
        group_users = {user for group in groups
                       for user in policy[group]['users']}
        total_users = ({user for group in groups
                        for user in policy[group]['users']} | set(users))
        for group in groups:
            display_usage_for_a_group(policy, group, kilobytes=args.kilobytes,
                megabytes=args.megabytes)
        for user in sorted(set(users) - set(group_users)):
            display_usage_for_a_user(user, kilobytes=args.kilobytes,
                megabytes=args.megabytes)
        display_total_usage_for_users(total_users, kilobytes=args.kilobytes,
            megabytes=args.megabytes)


def update_policy(policy_path, shared_memory, enact=False):
    policy = load_policy(policy_path)
    if policy['shared'] == shared_memory:
        return
    
    shared_memory_overage = shared_memory - policy['shared']
    
    if policy['free']['memory_limit'] - shared_memory_overage >= 16:
        policy['free']['memory_limit'] -= shared_memory_overage
        policy['shared'] = shared_memory
        dump_policy(policy, policy_path)
        if enact:
            enact_policy(policy)
            enact_policy(policy)
        return
    
    policy['free']['memory_limit'] = 16
    policy['shared'] = shared_memory
    for group in itertools.islice(
        itertools.cycle(get_group_set(policy) - {'free'}),
        shared_memory_overage - policy['free']['memory_limit'] + 16
    ):
        policy[group]['memory_limit'] -= 1
    dump_policy(policy, policy_path)
    if enact:
        enact_policy(policy)
        enact_policy(policy)
    

def update_shared(args):
    require_super_user()
    shared_memory = (shared_memory_in_gigabytes() if not args.shared
        else args.shared)
    update_policy(PROPOSED_POLICY_PATH, shared_memory)
    update_policy(CURRENT_POLICY_PATH, shared_memory, enact=True)


def parse_arguments():
    parser = ArgumentParser(
        description=('Display the current memory policy'))
    parser.add_argument('--version', action='version',
        version='%(prog)s {version}'.format(version=__version__))
    parser.set_defaults(func=lambda _: parser.print_help(sys.stdout))
    subparsers = parser.add_subparsers()

    parser_current = subparsers.add_parser('current',
        help='display the current memory policy')
    parser_current.set_defaults(func=mcurrent)

    parser_previous = subparsers.add_parser('previous',
        help='display the previous memory policy')
    parser_previous.set_defaults(func=mprevious)

    parser_proposed = subparsers.add_parser('proposed',
        help='display the proposed memory policy')
    parser_proposed.set_defaults(func=mproposed)

    parser_draft = subparsers.add_parser('draft',
        help='draft a memory policy proposal')
    parser_draft.add_argument('draft')
    parser_draft.set_defaults(func=mdraft)

    parser_enact = subparsers.add_parser('enact',
        help='enact the proposed memory policy')
    parser_enact.add_argument(
        '--no-daemon', action='store_true',
        help='Don\'t restart the daemon. (This is for use in setup).')
    parser_enact.set_defaults(func=menact)

    parser_free = subparsers.add_parser('free',
        help='free up memory in the proposed policy')
    parser_free.add_argument('-g', '--group',
        help='group to free memory from')
    parser_free.add_argument('-u', '--users',
        help='comma-separated list of users to free memory from')
    parser_free.set_defaults(func=mfree)

    parser_induct = subparsers.add_parser('induct',
        help='induct a new user into the memory policy')
    parser_induct.add_argument(
        '-u', '--users', default=getpass.getuser(),
        help='comma-separated list of users to induct')
    parser_induct.set_defaults(func=minduct)

    parser_repeal = subparsers.add_parser('repeal',
        help='repeal the last enacted memory policy')
    parser_repeal.set_defaults(func=mrepeal)

    parser_reserve = subparsers.add_parser('reserve',
        help='add a reservation to the proposed memory policy')
    parser_reserve.add_argument('memory_in_gigabytes', type=int)
    parser_reserve.add_argument('-g', '--group',
        help='group name for memory reservation')
    parser_reserve.add_argument('-u', '--users',
        help='comma-separated list of usernames for memory reservation')
    parser_reserve.set_defaults(func=mreserve)

    parser_retire = subparsers.add_parser('retire',
        help='retire a user from the memory policy')
    parser_retire.add_argument('-u', '--users', default=getpass.getuser(),
        required=True, help='comma-separated list of users to retire')
    parser_retire.set_defaults(func=mretire)
    
    parser_usage = subparsers.add_parser('usage',
        help='display memory usage for users or groups')
    parser_usage.add_argument('-g', '--groups',
        help='comma-separated list of groups for usage display')
    parser_usage.add_argument('-u', '--users',
        help='comma-separated list of usernames for usage display')
    display_group = parser_usage.add_mutually_exclusive_group()
    display_group.add_argument('-k', '--kilobytes', action='store_true',
        help='display usage in kilobytes')
    display_group.add_argument('-m', '--megabytes', action='store_true',
        help='display usage in megabytes')
    parser_usage.set_defaults(func=musage)

    parser_update_shared = subparsers.add_parser('update-shared',
        help='update the shared memory value in current and proposed policies')
    parser_update_shared.add_argument('--shared', type=int,
        help='impose a shared memory value for testing')
    parser_update_shared.set_defaults(func=update_shared)

    return parser.parse_args()

def main():
    args = parse_arguments()
    args.func(args)
