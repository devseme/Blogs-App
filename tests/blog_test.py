import unittest
from app.models import Blog


class TestPost(unittest.TestCase):
    def setUp(self):
        """
        Method that will run before every test
        """
        self.new_blog = Blog(
            user_id=1,
            category_id=1,
            title="Blog Title",
            content="Blog Content"
            
        )

    def test_instance(self):
        """
        Test to check if the post object is an instance of the Post class
        """
        self.assertTrue(isinstance(self.new_blog, Blog))

    def test_save_blog(self):
        """
        Test to save a posted blog
        """
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog_by_id(self):
        """
        Test to check if the get posted blog by id method is working
        """
        self.new_blog.save_blog()
        got_blog = Blog.get_blog(1)
        self.assertTrue(got_blog is not None)