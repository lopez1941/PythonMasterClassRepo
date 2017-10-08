# in this example, head in html is a tag, body is a tag, doctype is a tag. when you have those situations where
# you can 'is a' you're talking in terms of inheritance.  'head is a tag' and we see that in the code that it's
# inheriting from Tag.
# but an html doc 'has' all these things in it.  it 'has a' head tag; it 'has a' doctype tag.  in 'has a' situations
# you're dealing with composition.

class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = '' # DOCTYPE doens't have an end tag


class Head(Tag):
    """Accepts an arg for a doc title."""
    def __init__(self, title):
        doc_title = Title(title)
        super().__init__('head', doc_title)


class Body(Tag):
    def __init__(self):
        super().__init__('body', '')  # body contents will be built separately
        self.body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self.body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self.body_contents:
            self.contents += str(tag)

        super().display(file=file)


class Title(Tag):
    def __init__(self, title_contents):
        super().__init__('title', title_contents)


class HtmlDoc(object):
    """
    Optional to pass a title for the doc as an arg. that will be passed to the head class instantiation.
    Defaults to 'Welcome' if none specified
       """

    def __init__(self, title='Welcome'):
        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    my_page = HtmlDoc('this is my heading, dude!')
    my_page.add_tag('h1', 'Main Heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'this is a paragraph that will appear on the page')
    with open('test.html', 'w') as test_doc:
        my_page.display(file=test_doc)

