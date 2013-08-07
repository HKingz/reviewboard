    def testLongFilenames(self):
    def testDiffHashes(self):
class UploadDiffFormTests(TestCase):
        def get_file_exists(filename, revision, request):
        repository.get_file_exists = get_file_exists
    def test_mercurial_parent_diff_base_rev(self):
        """Testing that the correct base revision is used for Mercurial diffs"""
        diff = (
            '# Node ID a6fc203fee9091ff9739c9c00cd4a6694e023f48\n'
            '# Parent  7c4735ef51a7c665b5654f1a111ae430ce84ebbd\n'
            'diff --git a/doc/readme b/doc/readme\n'
            '--- a/doc/readme\n'
            '+++ b/doc/readme\n'
            '@@ -1,3 +1,3 @@\n'
            ' Hello\n'
            '-\n'
            '+...\n'
            ' goodbye\n'
        )
        parent_diff = (
            '# Node ID 7c4735ef51a7c665b5654f1a111ae430ce84ebbd\n'
            '# Parent  661e5dd3c4938ecbe8f77e2fdfa905d70485f94c\n'
            'diff --git a/doc/newfile b/doc/newfile\n'
            'new file mode 100644\n'
            '--- /dev/null\n'
            '+++ b/doc/newfile\n'
            '@@ -0,0 +1,1 @@\n'
            '+Lorem ipsum\n'
        )
        diff_file = SimpleUploadedFile('diff', diff,
                                       content_type='text/x-patch')
        parent_diff_file = SimpleUploadedFile('parent_diff', parent_diff,
                                              content_type='text/x-patch')
        repository = Repository.objects.create(
            name='Test HG',
            path='scmtools/testdata/hg_repo.bundle',
            tool=Tool.objects.get(name='Mercurial'))
        form = UploadDiffForm(
            repository=repository,
            files={
                'path': diff_file,
                'parent_diff_path': parent_diff_file,
            })
        self.assertTrue(form.is_valid())
        diffset = form.create(diff_file, parent_diff_file)
        self.assertEqual(diffset.files.count(), 1)
        filediff = diffset.files.get()
        self.assertEqual(filediff.source_revision,
                         '661e5dd3c4938ecbe8f77e2fdfa905d70485f94c')