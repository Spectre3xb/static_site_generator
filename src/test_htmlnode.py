import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            value="Click me",
            props={"href": "https://www.boot.dev", "target": "_blank"}
        )
        expected = ' href="https://www.boot.dev" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_single_prop(self):
        node = HTMLNode(tag="img", props={"src": "image.jpg"})
        expected = ' src="image.jpg"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="p", value="Hello")
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty_props(self):
        node = HTMLNode(tag="div", props={})
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_no_value_leaf_to_html(self):
        node = LeafNode("b", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_no_tag_leaf_to_html(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()

