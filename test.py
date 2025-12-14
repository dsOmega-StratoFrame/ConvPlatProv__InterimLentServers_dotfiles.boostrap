{

    'changed': False, 'stat': {'exists': False
    }, 'invocation': {'module_args': {'path': 'premium/Premium.git/.git', 'follow': False, 'get_checksum': True, 'get_mime': True, 'get_attributes': True, 'checksum_algorithm': 'sha1'
        }
    }, 'failed': False, 'item': {'changed': False, 'stat': {'exists': False
        }, 'invocation': {'module_args': {'path': 'premium/.git', 'follow': False, 'get_checksum': True, 'get_mime': True, 'get_attributes': True, 'checksum_algorithm': 'sha1'
            }
        }, 'failed': False, 'item': {'name': 'premium', 'url': 'git@gitlab.rutube.ru:frontend/premium.git', 'worktrees': [
                {'name': 'Master', 'symlink': {'src': 'Premium.git', 'dest': 'Master'
                    }
                },
                {'name': 'Main', 'symlink': {'src': 'Premium.git', 'dest': 'Main'
                    }
                },
                {'name': 'CurrentTask', 'branch': '_CurrentTask'
                },
                {'name': 'CurrentTask1', 'branch': '_CurrentTask1'
                },
                {'name': 'Review', 'branch': '_Review'
                }
            ]
        }, 'ansible_loop_var': 'item'
    }, 'ansible_loop_var': 'item'
}


{
    'changed': False,
    'stat': {'exists': False},
    'invocation': {'module_args': {'path': 'premium/Premium.git/.git', 'follow': False, 'get_checksum': True, 'get_mime': True, 'get_attributes': True, 'checksum_algorithm': 'sha1'}},
    'failed': False,
    'item': {
        'changed': False,
        'stat': {'exists': True, 'path': '/Users/apakalo/Projects/premium', 'mode': '0755', 'isdir': True, 'ischr': False, 'isblk': False, 'isreg': False, 'isfifo': False, 'islnk': False, 'issock': False, 'uid': 502, 'gid': 20, 'size': 320, 'inode': 59873854, 'dev': 16777235, 'nlink': 10, 'atime': 1765553883.3198836, 'mtime': 1765553882.8289826, 'ctime': 1765553882.8289826, 'wusr': True, 'rusr': True, 'xusr': True, 'wgrp': False, 'rgrp': True, 'xgrp': True, 'woth': False, 'roth': True, 'xoth': True, 'isuid': False, 'isgid': False, 'blocks': 0, 'block_size': 4096, 'device_type': 0, 'flags': 0, 'generation': 0, 'birthtime': 1765552637.0880244, 'readable': True, 'writeable': True, 'executable': True, 'pw_name': 'apakalo', 'gr_name': 'staff', 'mimetype': 'inode/directory', 'charset': 'binary', 'version': None, 'attributes': [], 'attr_flags': ''},
        'invocation': {
            'module_args': {'path': '/Users/apakalo/Projects/premium', 'follow': False, 'get_checksum': True, 'get_mime': True, 'get_attributes': True, 'checksum_algorithm': 'sha1'},
        },
        'failed': False,
        'item': {
            'name': 'premium',
            'url': 'git@gitlab.rutube.ru:frontend/premium.git',
            'worktrees': [{'name': 'Master', 'symlink': {'src': 'Premium.git', 'dest': 'Master'}}, {'name': 'Main', 'symlink': {'src': 'Premium.git', 'dest': 'Main'}}, {'name': 'CurrentTask', 'branch': '_CurrentTask'}, {'name': 'CurrentTask1', 'branch': '_CurrentTask1'}, {'name': 'Review', 'branch': '_Review'}],
        },
        'ansible_loop_var': 'item',
    },
    'ansible_loop_var': 'item',
}
