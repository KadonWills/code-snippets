CREATE OR REPLACE PACKAGE bit_util IS
  /**
  * Author  : Elucian Moise <br>
  * Purpose : BIT Logical operations for binary_integers<br>
  */

  -- instead of |
  FUNCTION bitor(a IN BINARY_INTEGER, b IN BINARY_INTEGER) RETURN BINARY_INTEGER;

  -- instead of & (faster)  
  FUNCTION bitxor(a IN BINARY_INTEGER, b IN BINARY_INTEGER) RETURN BINARY_INTEGER;

  -- instead of ~  
  FUNCTION bitnot(p IN BINARY_INTEGER) RETURN BINARY_INTEGER;
  
  -- return a mask exactly opposite of the p, where n is the number of bits to be used in the mask.  
  FUNCTION bitnot(p IN BINARY_INTEGER, n IN INTEGER) RETURN NUMBER;
  
  -- instead of <<  
  FUNCTION bitlsh(a IN BINARY_INTEGER, n IN BINARY_INTEGER) RETURN BINARY_INTEGER;

  -- instead of >>  
  FUNCTION bitrsh(a IN BINARY_INTEGER, n IN BINARY_INTEGER) RETURN BINARY_INTEGER;

END bit_util;
/
