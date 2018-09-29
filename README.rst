
Import this script to replace numpy's array with a (sub)class that does not
allow for array multiplication.  This prevents you from accidentally writing
:code:`array_1 * array_2` when you meant :code:`array_1.dot(array_1)` in order
to do matrix multiplication.
