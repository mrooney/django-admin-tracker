from tasktrack.test_helpers import ExtendedTestCase

class tasktrackTests(ExtendedTestCase):
    def test_404(self):
        self.assertStatus(404, '/foobar/')

    def test_home(self):
        self.assertStatus(200, '/')

