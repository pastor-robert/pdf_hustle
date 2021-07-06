"""
Use the PyPDF2 library to create a booklet.

References:
    - https://pythonhosted.org/PyPDF2

"""

import click
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

__author__ = "Rob Adams"
__copyright__ = "Rob Adams"
__license__ = "MIT"


def pageList(pageCount=8):
    """Returns a sequence of page sets, one set per output page.


    >>> list(pageList(8))
    [(7, 0), (1, 6), (5, 2), (3, 4)]

    :param pageCount: the number of input pages, defaults to 8
    :type pageCount: int

    :return: An ordered list of output pages, each of which contains
             multiple input pages
    :rtype: list(tuple)
    """

    for i in range(pageCount//2):
        if i%2:
            yield i, pageCount-i-1
        else:
            yield pageCount-i-1, i


def reformatStream(input_, output=None):
    """Convert PDF read stream to a booklet PDF

    :param input_: the input document
    :type input_: PyPDF2.PdfFileReader
    :param output: the output document. Will be created if ``None``. defaults to None
    :type output: PyPDF2.PdfFileWriter

    :return: The output document.
    :rtype: PyPDF2.PdfFileWriter
    """
    if output is None:
        output = PdfFileWriter()

    for lhs, rhs in pageList(input_.numPages):
        lhs = input1.getPage(lhs)
        rhs = input1.getPage(rhs)
        lhs.mergeTranslatedPage(rhs, lhs.mediaBox.getUpperRight_x(), 0, True)
        output.addPage(lhs)

    return output

@click.command()
@click.argument('ifname')
@click.argument('ofname')
def booklet(ifname, ofname):
    with open(ifname, "rb") as ifstream:
        writer = reformatStream(ifstream)
    with open(ofname, "wb") as ofstream:
        writer.write(ofstream)

@click.command()
@click.argument('pagecount', default=8, type=int)
def pageListCLI(pagecount):
    print(list(pageList(pagecount)))

