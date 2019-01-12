# Python 3 - XML Processing :

XML stands for eXtensible Markup Language.

XML was designed to store and transport data.

XML was designed to be both human- and machine-readable.

XML is a portable, open source language that allows programmers to
develop applications that can be read by other applications,
regardless of operating system and/or developmental language.


# What is XML?

The Extensible Markup Language (XML) is a markup language much like HTML or SGML.

This is recommended by the World Wide Web Consortium and available as an open standard.

XML is extremely useful for keeping track of small to medium amounts of data without
requiring a SQL-based backbone.

What is XML?
XML stands for eXtensible Markup Language
XML is a markup language much like HTML
XML was designed to store and transport data
XML was designed to be self-descriptive
XML is a W3C Recommendation

XML Does Not DO Anything
Maybe it is a little hard to understand, but XML does not DO anything.


<?xml version="1.0" encoding="UTF-8"?> # Decalartion
<Course>    # Root Element
    <CourseName>Python</CourseName>  # Child Element
        <CourseFee>10</CourseFee>    # Sub Child Element
    <CourseName>AWS</CourseName>
</Course>

# XML Parser Architectures and APIs :

The Python standard library provides a minimal but useful set of interfaces to work with XML.

The two most basic and broadly used APIs to XML data are the SAX and DOM interfaces.

#Simple API for XML (SAX) :
Here, you register callbacks for events of interest and then let the parser proceed
through the document.

This is useful when your documents are large or you have memory limitations,
it parses the file as it reads it from disk and the entire file is never stored in memory.

# Document Object Model (DOM) API :
This is a World Wide Web Consortium recommendation wherein the entire file is read
into memory and stored in a hierarchical (tree-based) form to represent all the features
of an XML document.

SAX obviously cannot process information as fast as DOM can when working with large files.

On the other hand, using DOM exclusively can really kill your resources,
especially if used on a lot of small files.

SAX is read-only, while DOM allows changes to the XML file.

Since these two different APIs literally complement each other,
there is no reason why you cannot use them both for large projects.