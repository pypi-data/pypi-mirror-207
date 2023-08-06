#! /usr/bin/env python3

import numpy as np

class SpinOp:
    """ 
    Class representing a spin operator, given by:
        SO = phase * product_operator
    It allows to represent pulses, delays, etc.
    ---------
    Attributes:
    - Op: 2darray
        Matrix representation of the associated product operator
    - phase: float
        Constant that multiplies the matrix
    """
    def __init__(self, Op, phase):
        """
        Initialize the class by storing Op and phase in the associated attributes.
        --------
        Parameters:
        - Op: 2darray
            Matrix representation of the associated product operator
        - phase: float
            Constant that multiplies the matrix
        """
        self.Op = Op
        self.phase = phase

    def __call__(self):
        """
        Return the matrix representation of the full operator, i.e. self.phase * self.Op
        """
        return self.phase * self.Op

    @staticmethod
    def commut(A, B):
        """
        Commutator between two operators A, B:
        [A,B] = AB - BA
        --------
        Parameters:
        - A: 2darray
            Matrix representation of operator A
        - B: 2darray
            Matrix representation of operator B
        --------
        Returns:
        - commutator: 2darray
            Computed commutator, rounded to the fifth decimal figure
        """
        commutator = A @ B - B @ A
        return np.around(commutator, 5)

    def evol(self, rho):
        """
        Evolution of rho due to the spin operator according to the commutator rule of product operators.
        In particular, defined rho = A and self.Op = B:
        > If A and B commute:
            A is returned
        > Else:
            returns A*cos(self.phase) + 1j[A,B]*sin(self.phase)
        --------
        Parameters:
        - rho: 2darray
            Operator you want to evolve
        --------
        Returns:
        - rho: 2darray
            Evolved operator
        """
        if self.commut(self.Op, rho).any() != 0:
            return np.around(rho * np.cos(self.phase), 5) + np.around(1j * self.commut(self.Op, rho) * np.sin(self.phase), 5)
        else:
            return np.around(rho, 5)

#---------------------------------------------------------------------------------------------------------------------------

class SpinState:
    """ 
    Class representing a spin state as linear combination of product operators.
    It consists of a dictionary whose keys are the product operators and the items are the associated coefficient of the LC.
    """
    def __init__(self, c):
        """ 
        Initialize the class with a given set of combinations, storing them into self.c
        -------
        Parameters:
        - c: dict
            Dictionary {prod_op : coeff}
        """
        self.c = c

    def __str__(self):
        """
        Prints the linear combination in a readable way.
        """
        string = []
        for op, coeff in self.c.items():
            string.append(self.print_operator(op, coeff))
        exp = ' '.join(string)
        return exp

    @staticmethod
    def print_operator(op, coeff):
        """
        Generates a string that express the linear combination.
        -------
        Parameters:
        - op: str
            Product operator
        - coeff: float
            Coefficient of the expansion
        -------
        Returns:
        - string: str
            String like f'{coeff:+.3f} {op}'
        """
        if coeff.imag == 0:
            return f'{coeff.real:+.3f} {op}'
        elif coeff.real == 0:
            return f'{coeff.imag:+.3f}j {op}'
        else:
            return f'({coeff.real:-.3f}{coeff.imag:+.3f}j) {op}'

class Proj_SOP:
    """
    Projection superoperator, used to decompose a density matrix into a linear combination of product operators.
    The projection coefficient c is defined as:
        c_i = Tr{< A | B_i >}
    where | B_i > is the i-th element of the basis, | A > is the density matrix to decompose, 
    < A | is the transposed conjugate of A, and Tr{W} is the trace of matrix W.
    """
    def __init__(self, basis):
        """
        Makes a shallow copy of the dictionary 'basis' and stores it into self.basis.
        -------
        Parameters:
        - basis: dict
            Dictionary of the form {operator : associated matrix}
        """
        self.basis = dict(basis)

    @staticmethod
    def proj(A, B):
        """
        Project A matrix on element B as Tr{< A | B >}
        --------
        Parameters:
        - A: 2darray
            Density matrix
        - B: 2darray
            Basis element
        ---------
        Returns:
        - c: float
            Projection coefficient round to the 5th decimal figure
        """
        dotprod = np.conj(A.T) @ B
        c = np.sum(np.diag(dotprod))        # Trace
        return np.round(c, 5)

    def proj_onbasis(self, A):
        """
        Loops on the basis elements and computes the projection coefficients.
        Then, returns a dictionary of the form { operator : coefficient}
        -------
        Parameters:
        - A: 2darray
            Density matrix
        -------
        Returns:
        - c: dict
            {operator:coefficient}
        """
        c = {}
        for Op, B in self.basis.items():
            c[Op] = self.proj(A, B)
        return c

    def __call__(self, A, only_nonzero=True):
        """
        Project A on self.basis using self.proj_onbasis
        -------
        Parameters:
        - A: 2darray
            Density matrix
        - only_nonzero: bool
            Discard the null coefficients (True) or keep them (False)
        -------
        Returns:
        - c: SpinState object
            SpinState object initialized with the computed coefficients
        """

        proj_coeff = self.proj_onbasis(A)   # dictionary

        if only_nonzero:
            tmp_c = dict(proj_coeff)    # Shallow copy to avoid 'shape change' error during for
            for op, coeff in tmp_c.items():
                if not coeff:       # it is zero
                    _ = proj_coeff.pop(op)  # Pop it out

        c = SpinState(proj_coeff)
        return c

    
#---------------------------------------------------------------------------------------------------------------------------

class Spin_05:
    """
    Class that represents a spin-1/2 in terms of product operators.
    --------
    Attributes:
    - Ip: 2darray
        I_+
    - Im: 2darray
        I_-
    - Ia: 2darray
        I_alpha
    - Ib: 2darray
        I_beta
    - ID: 2darray
        Identity
    - Ix: 2darray
        I_x
    - Iy: 2darray
        I_y
    - Iz: 2darray
        I_z
    """
    def __init__(self):
        """
        Compute the product operators in the cartesian basis as linear combination of single-element basis.
        """
        # Initialize single element basis
        self.Ip = np.array([    # I+
            [0, 1],
            [0, 0],
            ])
        self.Im = np.array([    # I-
            [0, 0],
            [1, 0],
            ])
        self.Ia = np.array([    # I alpha
            [1, 0],
            [0, 0],
            ])
        self.Ib = np.array([    # I beta
            [0, 0],
            [0, 1],
            ])

        # Cartesian basis
        self.Ix = ( self.Ip + self.Im ) /2
        self.Iy = ( self.Ip - self.Im ) /2j
        self.Iz = ( self.Ia - self.Ib ) /2
        self.ID = ( self.Ia + self.Ib ) 

#---------------------------------------------------------------------------------------------------------------------------


class SpinSys:
    """
    Class representing a set of coupled spins-1/2.
    Computes all the product operators and saves them as single attributes.
    They can also be accessed from self.PO: its keys are also the names of the attributes.
    The spins are labelled as I1, I2, ...

    To evolve the spin system according to a given spin operator, multiply the two object together with *.
    This will trigger the "evol" function of the spin operator.
    ---------
    Attributes:
    - PO: dict
        Product operators {po : matrix representation}
    - P: Proj_SOP object
        Projection operator for this spin system
    - rho: 2darray
        Density matrix
    """
    def __init__(self, *spins):
        """
        Make the product operators.
        -------
        Parameters:
        - spins: positional arguments
            Sequence of Spin_05 objects
        """
        nspins = len(spins)     # Number of coupled spins
        basis = 'ID', 'Ix', 'Iy', 'Iz'      # To be looped onto
        PO = {}     # Define empty dictionary
        for k, spin in enumerate(spins):
            if k == 0:  # Add the elements of the first spin to PO
                for op in basis:
                    if op == 'ID':
                        newkey = op
                    else:
                        newkey = op.replace('I', 'I1')
                    PO[newkey] = spin.__dict__[op]
            else:       # Expand PO with the product operators of the next spin
                tmp_PO = dict(PO)       # Shallow copy to avoid "dict changed size" error during for
                for key1, op1 in tmp_PO.items():    # Pre-existing PO
                    for key2 in basis:              # Next spin
                        op2 = spin.__dict__[key2]   
                        # Calculate the new label for the product operator
                        if 'ID' in key1 and 'ID' in key2:   
                            newkey = 'ID'
                        else:
                            if 'ID' in key1:
                                key1 = key1.replace('ID', '')
                            if key2 == 'ID':
                                key2 = ''
                            newkey = f'{key1}{key2.replace("I", f"I{k+1}")}'
                        PO[newkey] = np.kron(op1, op2)  # Make the kronecker product to calculate the next product operator
        # Store the operators in self.PO
        self.PO = PO
        
        # Correct the product operators with the normalization factor
        for key, value in PO.items():
            nfac = len(key) // 3    # One spin counts as three letters
            if nfac:    # Skip zero 
                value *= nfac
                PO[key] = value
            self.__dict__[key] = value

        # Initialize the projection superoperator with self.PO as basis
        self.P = Proj_SOP(self.PO)

        eqstate = [f'I{n+1}z' for n in range(nspins)]   # Magnetization along z
        # Density matrix
        self.rho = np.sum([self.__dict__[key] for key in eqstate], axis=0)

    def __mul__(self, other):
        """ 
        Multiplication. Changes self.rho according to what is other.
        In particular, if other is a SpinOP object, applies the product operator rule according to the method "evol" of SpinOP.
        """
        if isinstance(other, (int, float)): # number
            self.rho = other * self.rho     # product times a scalar
        elif isinstance(other, SpinOp):     # Spin Operator
            C = self.P(self.rho)    # Project the density matrix to decompose it into single product operators
            new_rho = []        # Empty list
            for selfop, self_coeff in C.c.items():  
                new_rho.append(self_coeff * other.evol(self.PO[selfop]))    # Evolve one operator at the time
            self.rho = np.sum(new_rho, axis=0)      # Put it back together
        elif isinstance(other, np.ndarray): # Matrix
            self.rho = other @ self.rho     # Matrix product
        else:   # Do nothing
            print('Unaltered.')
        return self.rho

    def __rmul__(self, other):
        """ Reverse multiplication. Calls self.__mul__ """
        self.__mul__(other)

    def __call__(self):
        """
        Return a shallow copy of self.rho
        """
        return np.copy(self.rho)

#---------------------------------------------------------------------------------------------------------------------------
