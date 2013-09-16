from reviewboard.diffviewer.processors import (filter_interdiff_opcodes,
                                               merge_adjacent_chunks)
from reviewboard.testing import TestCase
                          ("equal", 0, 6, 2, 8)])
                         [("equal", 0, 4, 0, 4),
                          ("insert", 5, 5, 5, 9),
                          ("equal", 5, 8, 9, 12)])
            self.assertTrue(file.origFile.startswith("%s/orig_src/" %
            self.assertTrue(file.newFile.startswith("%s/new_src/" %
    fixtures = ['test_scmtools']
            'diff --git a/README b/README\n'
            'index d6613f5..5b50866 100644\n'
            '--- README\n'
            '+++ README\n'
            'diff --git a/README b/README\n'
            'index d6613f5..5b50866 100644\n'
            '--- README\n'
            '+++ README\n'
        repository = self.create_repository(tool_name='Test')
                          '<span class="hl">abc</span>')
                          '<span class="hl">a</span>bc')
    fixtures = ['test_scmtools']
        repository = self.create_repository()
        repository = self.create_repository()
            'diff --git a/README b/README\n'
            'index d6613f5..5b50866 100644\n'
            '--- README\n'
            '+++ README\n'
        repository = self.create_repository(tool_name='Test')
                    call_fake=lambda *args, **kwargs: True)
            'diff --git a/README b/README\n'
            'index d6613f5..5b50866 100644\n'
            '--- README\n'
            '+++ README\n'
        repository = self.create_repository(tool_name='Test')
                    call_fake=lambda *args, **kwargs: True)
                'base_commit_id': '1234',
        self.assertEqual(diffset.basedir, '/')
        self.assertEqual(diffset.base_commit_id, '1234')
        def get_file_exists(repository, filename, revision, *args, **kwargs):
            'diff --git a/README b/README\n'
            'index d6613f5..5b50866 100644\n'
            '--- README\n'
            '+++ README\n'
            'diff --git a/README b/README\n'
            'index d6613f4..5b50865 100644\n'
            '--- README\n'
            '+++ README\n'
            'diff --git a/UNUSED b/UNUSED\n'
            'index 1234567..5b50866 100644\n'
            '--- UNUSED\n'
            '+++ UNUSED\n'
        repository = self.create_repository(tool_name='Test')
        self.assertTrue(('/README', 'd6613f4') in saw_file_exists)
        self.assertFalse(('/UNUSED', '1234567') in saw_file_exists)