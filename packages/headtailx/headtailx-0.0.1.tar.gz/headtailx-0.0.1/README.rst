=========
headtailx
=========

*Mitchell P. Krawiec-Thayer*

This library provides ``headx`` and ``tailx`` commands which behave similarly to the ``head`` and ``tail`` commands, extended with support for binary data formats.

Supported file types include:

- Feather files
- Pickle files
- Parquet files
- HDF5 files
- XLSX

Example
=======

Let's compare ``head`` and ``headx`` for a Feather file. Here's the standard ``head`` command:

.. code-block:: bash

    $ head test.feather -n 4

    ARROW1����H

The above output is binary data, which is not very useful. Now let's try ``headx``:

.. code-block:: bash

    $ headx -n 4 data.feather

     timestamp  flavor color  foobar
        10 strange   red       9
        20      up  blue       8
        30   charm  None       7

Installation
============

To install ``headtailx``, simply run:

.. code-block:: bash

    pip install headtailx
    
    
Use
===

Simply replace ``head`` with ``headx`` (and likewise ``tail`` -> ``tailx``) when previewing binary data formats. For example ``headx <filename> -n 3`` would show the first 3  lines.    


License
=======

This project is licensed under the MIT License. See the LICENSE file for more information.
