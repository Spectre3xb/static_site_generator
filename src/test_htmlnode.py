import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from main import *
from textnode import *



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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

        def test_to_html_with_grandchildren(self):
            grandchild_node = LeafNode("b", "grandchild")
            child_node = ParentNode("span", [grandchild_node])
            parent_node = ParentNode("div", [child_node])
            self.assertEqual(
                parent_node.to_html(),
                "<div><span><b>grandchild</b></span></div>",
            )

        def test_parent_no_tag(self):
            node = ParentNode(None, [LeafNode("p", "child")])
            with self.assertRaises(ValueError):
                node.to_html()

        def test_parent_no_children(self):
            node = ParentNode("div", None)
            with self.assertRaises(ValueError):
                node.to_html()

        def test_parent_empty_children_list(self):
            node = ParentNode("div", [])
            self.assertEqual(node.to_html(), "<div></div>")

        def test_parent_with_multiple_children(self):
            node = ParentNode(
                "div",
                [
                    LeafNode("p", "First paragraph"),
                    LeafNode("p", "Second paragraph"),
                    LeafNode("p", "Third paragraph")
                ]
            )
            expected = "<div><p>First paragraph</p><p>Second paragraph</p><p>Third paragraph</p></div>"
            self.assertEqual(node.to_html(), expected)

        def test_parent_with_props(self):
            node = ParentNode(
                "div",
                [LeafNode("p", "Hello")],
                {"class": "container", "id": "main"}
            )
            expected = '<div class="container" id="main"><p>Hello</p></div>'
            self.assertEqual(node.to_html(), expected)

        def test_parent_with_mixed_children(self):
            node = ParentNode(
                "div",
                [
                    LeafNode(None, "Raw text"),
                    LeafNode("b", "Bold text"),
                    ParentNode("p", [LeafNode("i", "Italic in paragraph")])
                ]
            )
            expected = "<div>Raw text<b>Bold text</b><p><i>Italic in paragraph</i></p></div>"
            self.assertEqual(node.to_html(), expected)

        def test_deeply_nested_structure(self):
            node = ParentNode(
                "div",
                [
                    ParentNode(
                        "section",
                        [
                            ParentNode(
                                "article",
                                [
                                    LeafNode("h1", "Title"),
                                    LeafNode("p", "Content")
                                ]
                            )
                        ]
                    )
                ]
            )
            expected = "<div><section><article><h1>Title</h1><p>Content</p></article></section></div>"
            self.assertEqual(node.to_html(), expected)

        def test_parent_with_leaf_children_with_props(self):
            node = ParentNode(
                "ul",
                [
                    LeafNode("li", "Item 1", {"class": "first"}),
                    LeafNode("li", "Item 2"),
                    LeafNode("li", "Item 3", {"class": "last"})
                ]
            )
            expected = '<ul><li class="first">Item 1</li><li>Item 2</li><li class="last">Item 3</li></ul>'
            self.assertEqual(node.to_html(), expected)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    if __name__ == "__main__":
        unittest.main()

if __name__ == "__main__":
    unittest.main()

