import math

class Vector(object):
  """ a class that contains basic vector operations and comparisons """
  def __init__(self, *values):
    """ 
    the constructor for the Vector class
    :param *values: variable length argument list of ints or floats 
    :return: n/a for constructors 
    """

    # task 1.b.i
    # was previously self.data - because of the __getitem__ function, ALL of our self.data now can be just self (__init__ has to be self.data)
    self.data = [] # holding an empty list for our inputs (do not use self here)
    for value in values: # for each value input
      if isinstance(value, (int, float)): # if user input is an int or a float, then
        self.data.append(float(value)) # attach value (or next value) to the list
      else: # if user input is another type
        raise TypeError('Only int and floats can be arguments for vectors.') # raise Type Error
    

    # task 1.b.ii
    self.dim = len(self.data) # storing the length of self.data into self.dim

    #task 1.c.i
    if self.dim == 2: # if the length of our self.data is 2
      self.__class__ = Vector2 # use the Vector2 class
    if self.dim == 3:  # if the length of our self.data is 3
      self.__class__ = Vector3 # use the Vector3 class
    # can still accept vectors of a larger size
    


  #task 1.c.ii
  def __str__(self):
    """
    return a string representation of the Vector
    :param: self, an instance of the Vector class
    :returns: returns a string of the Vector in the form "<Vector{length} = float, float, float...>"
    """
    values = ''   # empty space for strings later
    for value in self:  # for each value in self
      values = values + str(value) + ', '   # values gains a string input of the current value in the loop and a comma 
    return f'<Vector{self.dim}: {values[:-2]}>' # returns the string of values and gets rid of the last two entries in the string
                          # ", " from the for loop


  #task 1.c.iii											
  def __len__(self):
    """
    return the number of entries in the Vector
    :param: N/A
    :returns: returns the length of the Vector instance 
    """
      
    return self.dim # returns the length of self


  #task 1.c.iv part 1
  def __getitem__(self, index):# getitem function returns an index value of the instance
    """
    returns the index value requested of the instance of the Vector class
    :param index: the index is an integer
    :return: returns the float value at position index
    """

    #This slight modification will make the looping by value work correctly. -rds
    if isinstance(index, int):
      if -self.dim <= index < self.dim:
        return self.data[index]
      raise IndexError
    return TypeError('The position must be an integer index in range.')
    # need to check that index is in range
    #if -self.dim <= index < self.dim: # if index value is between (or equal to) the negative and positive values for self.dim
      #return self.data[index] # return the given value at position of index in self.data
    #else:
      # if index is out of range, raise ValueError
      #raise ValueError('Index value must be greater than or equal to -self.dim and less than or equal to self.dim')


  # task 1.c.iv part 2
  def __setitem__(self, index, value):
    """
    changes the value of self at position index with a new value
    :param index: index is an integer
    :param value: the value is an int or a float
    :return: return new self with changed value at the specified index
    """
    if -self.dim <= index < self.dim: # if index value is between (or equal to) the negative and positive values for self.dim
      if isinstance(value, (int, float)): # if the new user input value is an int or float
        self[index] = float(value)  # change the current value at this index position to the new value
                            # and change this value to a float
      else:
        raise TypeError('Vector entries can only be of type int or float') # if user input is not correct
    else:
      # if index is out of range, raise ValueError
      raise IndexError('Index value must be greater than or equal to -self.dim and less than or equal to self.dim')


  # task 1.c.v
  def __eq__(self, other):
    """
    overloading the == operator to compare two vectors for equality
    :param other: another Vector instance
    :return: True, if all Vector parameters are equal; False otherwise
    """
    if not isinstance(other, Vector) or self.dim != other.dim: # if other is not a vector
      return False													# or if the lengths are not equal, return False
    for i in range(self.dim): # for each index i in the range of the length of the instance
      if self[i] != other.data[i]: # if the index value at the ith position is not equal 
        return False	# return False
      return True             # otherwise, return True
    


  # task 1.c.vi - return a deep copy of the vector
  def copy(self):
    """
    return a deep copy of the instance of the Vector class
    :param: N/A
    :return: a Vector instance that is a deep copy of the origianl Vector instance
    """
    temp = [] # holding an empty list for the vector deep copy
    for value in self: # for each vector entry in self
      temp.append(value) # add that value to the temp list
    return Vector(*temp) # return this list - * makes it so it doesn't have to be specified as a specific type (list/ tuple)


  # task i.c.vii
  def __mul__(self, other):
    """
    multiplies the vector by a scalar on the right
    :param other: a scalar of type int or float
    :return: a new Vector instance resulting from scalar multiplication
    """
    if isinstance(other, (int, float)): # if other is a int or a float
      temp = [] # holds space for new vector
      for value in self: # for each entry in our vector 
        temp.append(value * other) # add the multiplied entry to the temp list
      return Vector(*temp) # return this list as a Vector
    else:
      return NotImplemented	# if other is not a int or float, return this


  # task i.c.viii
  def __rmul__(self, other):
    """
    multiplies the vector by a scalar on the left
    :param other: a scalar of type int or float
    :returns: a new Vector instance resulting from scalar multiplication
    """
    return self * other # using the __mul__ method after python notices the scalar is on the left


  # task i.c.ix - addition
  def __add__(self, other):
    """
    performs vector addition with another Vector instance
    :param other: another vector instance to add
    :returns: a new Vector instance resulting from the addition
    """
    if self.dim != len(other): # if the vectors are not the same length
      raise ValueError('Vector addition/subtraction requires vectors to be the same length') # raise value error
    temp = [] # holding a spot for the new vector
    for i in range(self.dim): # for each entry in the vector 
      result = self[i] + other[i] # store the result of adding entry i of self to the entry i of other
      temp.append(result) # append this result to the temp list
    return Vector(*temp) # return the temp list as a Vector

#Once you have created __add__ and __neg__, there is a much better way to create __sub__. Do you see what you should do?
      
  # task i.c.x - subtraction
  def __sub__(self, other):
    """
    performs vector subtraction with another Vector instance
    :param other: another Vector instance to subtract
    :returns: a new Vector instance resulting from the subtraction
    """
    # if self.dim != len(other): # if the vectors are not the same length
    #   raise ValueError('Vector subtraction requires vectors to be the same length') # raise value error
    
    return self + -other 
    # temp = [] # holding a spot for the new vector
    # for i in range(self.dim): # for each entry in the vector 
    #   result = self[i] - other[i] # store the result of subtracting entry i of self by the entry i of other
    #   temp.append(result) # append this result to the temp list
    # return Vector(*temp) # return the temp list as a Vector

  # task i.c.xi - negation
  def __neg__(self):
    """
    returns the negation of a vector instance
    :param: N/A
    :return: a new Vector instance with negated values
    """
    temp = [] # hold spot for new vector
    for i in range(self.dim): # for each index in the length of self 
      result = (-1) * self[i]	 # multiply each entry in self by (-1) and store in result
      temp.append(result) # add each result to the temp list
    return Vector(*temp)	# return this list as a Vector



  # task i.c.xii - truedivision
  def __truediv__(self, other):
    """ 
    divides the Vector instance by a scalar
    :param other: a scalar of type int or float that is not zero
    :return: returns a Vector instance where each entry is divided by the scalar
    """
    if not isinstance (other, (int, float)): # if other is not an int or a float
      raise TypeError('Vectors can only be divided by ints or floats') # raise TypeError
    elif other == 0: # if other is equal to 0
      raise ValueError('You cannot divide by 0') # raise ValueError
    else:
      temp = [] # storing space for the new list
      for i in range(self.dim): # for each entry in self
        result = self[i] / other  # divide the entry by other and store this in result 
        temp.append(result) # add the result to the list temp
      return Vector(*temp) # return the list as a vector



  # task i.c.xiii - norm(self, p)
  def norm(self, p):
    """
    calculates the p-norm of the Vector instance
    :param p: p can be a positive int, or the string 'infinity'
    :return: the p-norm of the Vector instance as a float
    """
    if isinstance(p, str): # if p is a string
      if p == 'infinity': # if p is equal to the string infinity
        temp = [] # store 'infinity norm' into temp
        for i in self: # for each entry in self
          temp.append(abs(i)) # append the absolute value of each entry in the temp list
        return max(temp) # return the maximum value of temp
      else: # if p is a string but does not have the value 'infinity'
        raise ValueError('Only infinity can be a string input for p') # raise a Value Error
    elif isinstance(p, int): # if p is an int value
      if p <= 0: # error checking - if p is less than or equal to zero 
        raise ValueError('p can only be a positive int, greater than 0') # raise value Error
      else: # if p > 0
        temp = 0 # set temp to 0 to start
        for i in range(self.dim): # for each entry index position in self
          result = abs(self[i])**p  # store the absolute value of the index entry to the pth power in the result variable
          temp = temp + result # add this result variable to temp
          # continue to add each result to temp (so temp is one number at the end)
        return temp**(1/p) # return the pth root of the value in temp after the for loop is completed
    else: # if p is something that has not already been checked for
      raise TypeError('p must either be infinity or a positive non-zero integer to calculate the norm of a vector')


# task 4.a - 2 norm of a vector
  @property
  def mag(self):
    """
    calculate the 2-norm, or magnitude, of the Vector instance
    :param: N/A
    :return: the 2-norm of the Vector instance as a float
    """
    temp = 0 # temp is set to 0 because the 2-norm is a number value	
    for value in self: # for each value in self
      sqvalue = value**2 # set value to be the square of the value
      temp = temp + sqvalue # add the last result to temp
    return temp**(1/2) # return the value of temp raised to the 1/2 power (or take the sq root of temp)


# task 4.b - return the square of the 2-norm without using any square roots
  @property
  def mag_squared(self):
    """
    calculate the square of a 2-norm without using any square roots
    :param: N/A
    :return: the square of the 2-norm of the Vector instance as a float 
    """
    temp = 0 # start temp at 0
    for value in self: # for each entry in our vector
      temp = temp + value**2 # temp is replaced by current temp value + the square of the value
    return temp
    #basically the same as 4.a but without the temp**(1/2) at the end



# task 4.c - returns a unit vector in the same direction as this vector
  @property
  def normalize(self):
    """
    normalizes the vector instance to a unit vector in the same direction as the previous one
    :param: N/A
    :return: a new Vector instance representing the unit vector in the same direction 
    """
    if self.mag == 0: # if the magnitude of our vector instance is 0
      raise ValueError('You cannot divide by 0') # raise a ValueError - cannot divide by 0
    else:
      scalar = 1/self.mag # create the scalar by taking 1 divided by the magnitude of the vector
      return scalar*self # multiply the scalar by our vector (uses the multiplication method above)  
                # to return the normalized vector



# task 4.d - returns true if the vector is identically the zero vector of the appropriate dimension, false otherwise
  @property
  def is_zero(self): 
    """
    checks if the Vector instance is the zero vector
    :param: N/A
    :return: True if the vector is the zero vector; False otherwise
    """
    if self.mag_squared != 0: # if the magnitude is not 0
      return False # return False
    else: 
      return True # otherwise, return True


# task 4.e - returns a tuple of the coordinates of this vector converted to integers
  @property
  def i(self):
    """
    returns a tuple of the coordinates of the Vector instance converted to integers
    :param: N/A
    :returns: a tuple of the Vector coordinates as integers
    """
    temp = [] # empty space for the list
    for value in self:  # for each value in self
              # can use just self instead of self.data because 
      # change the value to an int and assign it to value
      temp.append(int(value)) # add this result to the temp list 
                  # quicker than result = temp + int(value)
                  # temp = temp + result
    return tuple(temp) # return a tuple of the list created in temp


# task 2
# task 2.a
class Vector2(Vector):
  """
  a Vector subclass for a vector of length 2
  """

  def __init__(self, x, y):
    """ 
    the constructor method for the Vector2 class
    :param x: the x value for the vector
    :param y: the y value for the vector
    :return: a Vector instance that is both Vector and Vector2
    """

    super().__init__(x,y) # call the constructor for the super class (the Vector class) to create our Vector2


  # task 2.b.i (getter property for x)
  @property # properties help things feel like attributes rather than functions
  def x(self):            # functions with alot of calculations should stay a regular function call rather than a property
    """
    getter property for the x-component of the Vector3 instance
    :param: N/A
    :return: the x-component of the vector (value in position 0)
    """

    return self[0] # can use this because we have created our 'get item' method already
    # gets rid of the need to use self.data

  # task 2.b.ii (getter property for y)
  @property
  def y(self):
    """
    getter property for the y-component of the Vector3 instance
    :param: N/A
    :return: the y-component of the vector (value in position 1)
    """
    return self[1]
  


  # task 2.b.iii (setter property for x)
  @x.setter
  def x(self, newvalue):
    """
    setter property for the x-component of the Vector3 instance
    :param newvalue: the new value to assign to the x-component
    :returns: N/A
    """

    # would call this by stating 'newvector.x = #'
    if isinstance(newvalue, (int, float)): # if our new value is an int or a float
      self[0] = float(newvalue) # change the current index entry in self (our x) to the float value of 'newvalue'
    
    else: # if newvalue is not an int or a float
      raise TypeError('Only integer or float values can be accepted.')	# raise type error


  # task 2.b.iv (setter property for y)								
  @y.setter
  def y(self, newvalue):
    """
    setter property for the y-component of the vector
    :param newvalue: the new value to assign to the y-component
    :returns: N/A
    """

    if isinstance(newvalue, (int, float)):
      self[1] = float(newvalue)
    else: 
      raise TypeError('Only values of int or float can be accepted')
  
      
  # task 5.a - returns the degree measure of this cartesian vector in polar space    
  @property
  def degrees(self):
    """
    returns the degree measure of the cartesian vector in polar space
    :param: N/A
    :returns: the degree measure of the cartesian vector in polar space
    """
    if self.x == 0: # if x coordinate is 0, we have three cases
      if self.y > 0: # if y is a positive value, 
        return 90	# return 90
      elif self.y < 0: # if y is a negative value, 
        return -90 # return -90
      else: # if self.y == 0 
        return ValueError('The direction of the zero vector is undefined')
    else: # if x is not 0,
  
      theta = math.atan(self.y/self.x) # calculate theta using arctan(y/x)
                  # atan will return radians, need to multiply by 180/math.pi to convert
      if self.x < 0: # if our x is negative 
        theta = theta + 180 # add 180 degrees to fix the angle for coordinate II and III (arctan returns values in I and IV)
      return theta*180/math.pi # returning theta converted to degrees
# The function math.atan2(y, x) knows which quadrant the point is in so there is less need for post-processing the value that is returned.


  # task 5.b - returns the radian measure of this cartesian vector in polar space
  @property
  def radians(self):
    """
    returns the radian measure of the cartesian vector in polar space
    :param: N/A
    :returns: the radian measure of the cartesian vector in polar space
    """
    return self.degrees*(math.pi/180) 


  # task 5.c - returns a vector2 perpendicular to this vector (only one calculation should be made)
  @property
  def perpendicular(self):
    """
    returns a Vector2 instance perpendicular to this vector
    :param: N/A 
    :return: a Vector2 instance perpendicular to this vector
    """
    return Vector2(-self.y, self.x) 
    

# task 3.a
class Vector3(Vector):
  """
  a subclass of the Vector class that has three vector entries for a Vector3 instance
  """

  def __init__(self, x, y, z):
    """
    a constructor method for the Vector3 class
        :param x: int or float, x-coordinate of the Vector3 instance.
        :param y: int or float, y-coordinate of the Vector3 instance.
        :param z: int or float, z-coordinate of the Vector3 instance.
    :returns: n/a returns for constructors
    """

    super().__init__(x, y, z)


# task 3.b.i - getter methods for x, y, and z

  # getter method for x in Vector3
  @property
  def x(self):
    """
    getter method for the x-coordinate of the Vector3 instance
    :return: the x-coordinate of the Vector3 instance
    """

    return self.data[0] # return the x value (index 0)

  # getter method for y in Vector3
  @property
  def y(self):
    """
    getter method for the y-coordinate of the Vector3 instance
        :returns: the y-coordinate of the Vector3 instance
    """

    return self.data[1] # return the y value (index 1)

  # getter method for z in Vector3
  @property
  def z(self):
    """
    getter method for the z-coordinate of the Vector3 instance
    :return: the z-coordinate of the Vector3 instance
    """

    return self.data[2] # return the z value (index 2)

  

# task 3.b.ii - setter methods for x, y, and z

  #setter method for x in Vector3
  @x.setter # forgot this part 
  def x(self, newvalue):
    """
    setter method for the x-coordinate of the Vector3 instance
    :param newvalue: int or float, new value for the x-coordinate
    :return: N/A - setter method does not have a return value
    """

    if isinstance(newvalue, (int, float)): # if newvalue is an int or float
      self[0] = float(newvalue) # store the float type of newvalue in the 0 index of self
    else: # if newvalue is not an int or a float
      raise TypeError('Vectors can only have int or float entries') # raise a typeerror


  @y.setter
  def y(self, newvalue): 
    """
    a setter method for the y-coordinate of the Vector3 instance
    :param newvalue: int or float, new value for the y-coordinate
    :returns: n/a - setter method does not have a return value
    """

    if isinstance(newvalue, (int, float)): # if newvalue is an int or float
      self[1] = float(newvalue) # store the float type of newvalue in the 1 index position of self
    else: # if newvalue is not an int or a float
      raise TypeError('Vectors can only have int or float entries') # raise type error


  @z.setter
  def z(self, newvalue):
    """
    a setter method for the z-coordinate of the Vector3 instance
    :param newvalue: int or float, new value for the z-coordinate
    :returns: n/a - setter method does not have a return value
    """

    if isinstance(newvalue, (int, float)): # if newvalue is an int or a float
      self[2] = float(newvalue) # store the float value of newvalue in the 2 index position of self
    else: # if newvalue is not an int or a float
      raise TypeError('Vectors can only have int or float entries') # raise type error
  
  



# task 6.a
def dot(v, w): # don't want to use self, other --> self is reserved for class methods
  """ 
  compute the dot product of two vectors
  :param v: an instance of the Vector class
  :param w: another Vector instance
  :returns: the dot product of v and w
  """
  if v.dim != len(w): # if the lengths of the vectors v and w are not the same 
    raise ValueError('Vectors must be the same length to compute the dot product.') # raise value error
  else:
    temp = 0 # set temp = 0
    for i in range(v.dim):  # for each i in the range of the dimension of v
      temp = temp + v[i] * w[i] # add the multiplication of the ith index position of v and w in result to the current temp value
    return temp # return temp after for loop is completed


# task 6.b - cross product of two vector3 instances

def cross(v, w):
  """
  compute the cross product of two Vector3 instances
  :param v: a Vector3 instance
  :param w: another Vector3 instance
  :return: a Vector3 instance, the cross product of v and w
  """

  if not isinstance(v, Vector3) or not isinstance(w, Vector3):
    raise TypeError('Cross product requires three-dimensional vectors')

  else:
    a, b, c = v.x, v.y, v.z # using the getter methods and multiple assignment in python to assign
                    # a to the vector v x value, b to the vector v y value, and c
                    # to the vector v z value
    d, e, f = w.x, w.y, w.z

    rx = b*f - c*e # first entry of vector cross product result (have to explicitly use * to show multiplication of variables)
    ry = c*d - a*f # second entry of vector cross product result
    rz = a*e - b*d # third entry of vector cross product result

    return Vector3(rx, ry, rz) # return a Vector3 instance of the cross product of v and w


# task 6.c - polar coordinates

def polar_to_Vector2(r, theta): 
  """
  convert polar coordinates of a 2D point to a Vector2 instance
  :param r: float, the radius or distance from the origin
  :param theta: float, the angle in radians
  :returns: a Vector2 instance respresenting the polar coordinates
  """

  x = math.cos(theta)*r # x is the cos(theta)*r
  y = math.sin(theta)*r # y is the sin(theta)*r
 
  return Vector2(x, y) # return the x and y coordinates as a Vector2 instance










