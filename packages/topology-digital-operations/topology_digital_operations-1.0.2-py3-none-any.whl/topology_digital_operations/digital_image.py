 #HEADER
__author__ = "Karim Omar Jerez Santana"
__credits__ = ['Gregory Lupton', 'John Oprea', 'Nicholas A. Scoville']

#NEEDED LIBS
import matplotlib.pyplot as plt
import numpy as np
import re
import itertools
from math import floor

#CLASSES
class digital_image():
    """
    Class which represents a digital image.
    It contains some methods which are
    usual operations in these objects.
    
    Parameters:
        elements: List of tuples.
            List of elements represented by
            a tuple.
        defined_digital_image: string.
            String with pattern: I{number}
            (digital interval of length number)
            or D{number} (n-sphere digital version).
        
    Attributes:
        elements: Dict.
            Dictionary which the key is an 
            element from the digital image 
            given and its value is a list 
            with correspondant adjacent 
            elements (tuples).
        
    """
    def __init__(
            self,
            elements,
            defined_digital_image
            ):
        
        self.elements = {}
        
        if elements == None and defined_digital_image == None: 
            print('Generic digital image has been created')
            
        elif bool(re.search("[D][0-9]*", defined_digital_image)) == True and elements == None:
            n = int(defined_digital_image[1:])
            elements = __class__.generate_digital_sphere(n)
        elif bool(re.search("[I][0-9]*", defined_digital_image)) == True and elements == None:
            n = int(defined_digital_image[1:])
            elements = __class__.generate_interval(n)
        else:
            print('Elements have been read successfully!')
            
        if elements != None or defined_digital_image != None:
        
            for element in elements:
                self.elements[element] = []
            
            self.adj_elements_find()
    
    @staticmethod
    def generate_interval(n):
        """
        Static method which generates
        a list of 1-tuples which represents
        digital interval of length n.
        
        Parameters:
            n: int.
                Length of interval.
            
        Returns:
            elements: List of tuples.
                List of 1-tuples which represents
                elements from digital interval 
                of length n.
            
        """
        elements = [tuple([i]) for i in range(n+1)]
        return elements
    @staticmethod
    def generate_digital_sphere(n):
        """
        Static method which generates
        a list of (n+1)-tuples which 
        represents the n digital sphere.
        
        Parameters:
            n: int.
                Sphere dimension.
                 
        Returns:
            elements: List of tuples.
                List of (n+1)-tuples which represents
                elements from n digital sphere.
            
        """
        zero_element = [0]*(n+1)
        elements = []
        for i in range(len(zero_element)):
            positive_element = zero_element.copy()
            positive_element[i] = 1
            elements.append(tuple(positive_element))
            negative_element = zero_element.copy()
            negative_element[i] = -1
            elements.append(tuple(negative_element))
        return elements
    @staticmethod 
    def distance_btw_numbers_less_one(number_1, number_2):
        """
        Static method which checks if distance
        between numbers is less than one.
        
        Parameters:
            number_1: int.
            number_2: int.
                     
        Returns:
            Boolean.
            
        """
        if abs(number_2-number_1)<=1:
            return True
        else:
            return False
    
    @staticmethod
    def adj_checker(element_1, element_2):
        """
        Static method which checks two elements
        are adjacent.
        
        Parameters:
            element_1: tuple.
            element_2: tuple.
               
        Returns:
            Boolean.
            
        """
        if type(element_1) == 'int' and type(element_2) == 'int':
            return distance_btw_numbers_less_one(number_1, number_2)
        else:

            tuple_len = len(element_1)
            element_insp = 0
            while element_insp<=tuple_len-1:
                check = __class__.distance_btw_numbers_less_one(
                    element_1[element_insp], 
                    element_2[element_insp]
                    )
                
                if check == False:
                    return False
                element_insp+=1
            return True
           
    def adj_elements_find(self):
        """
        Method which fills elements attribute.
        
        Parameters:
            None.
        Returns:
            None.
        """
        elements_as_list = list(self.elements)
        for element_1 in elements_as_list:
            for element_2 in elements_as_list:
                if element_1==element_2:
                    continue
                else:
                    adj_check = __class__.adj_checker(element_1, element_2)
                    if adj_check == True:
                        self.elements[element_1].append(element_2)
    
    @staticmethod
    def subdivision(k, elements):
        """
        Method which finds k subdivision
        of a digital image.
        
        Parameters:
            k: int.
                Subdivision number.
            elements: list of tuples.
                Elements which are going
                to be subdivided.
            
        Returns:
            subdivision_elements: List 
            of tuples.
                Elements from subdivision.
        """
        subdivision_elements = []
        for element in elements:
            new_elements_gen = []
            for sub_element in element:
                poss_sub_element = []
                for n in range(k):
                    poss_sub_element.append(k*sub_element+n)
                new_elements_gen.append(poss_sub_element)
            cp = itertools.product(*new_elements_gen)
            for new_element in cp:
                subdivision_elements.append(new_element)
        return subdivision_elements
    
    @staticmethod 
    def partial_projection_number(k, number):
        """
        Static method which makes partial
        projection on number.
        
        Parameters:
            k: int.
                Initial subdivision which 
                is considered.
            number: int.
                Number to project.
                  
        Returns:
            new_number: int.
                maps of original number
                through partial projection.
        """
        x = number//k
        j = number % k
        if j>= 0 and floor(k/2)-1>=j:
            new_number = (k-1)*x+j
        if j>= floor(k/2) and j<=k-1:
            new_number = (k-1)*x+j-1
        return new_number
            
    @staticmethod 
    def project_element(
            k, 
            element, 
            projection_type
            ):
        """
        Static method which projects
        an element.
        
        Parameters:
            k: int.
                Initial subdivision which 
                is considered.
            element: tuple.
                Element to map.
            projection_type: str.
                Type of projection selected.
                It can be canonical or partial.
            
        Returns:
            new_element: tuple.
                maps of original element
                through selected projection.
        """
        new_element = []
        for number in element:
            if projection_type == 'canonical':
                new_number = floor(number/k)
            elif projection_type == 'partial':
                new_number = __class__.partial_projection_number(k, number)
            new_element.append(new_number)
        return tuple(new_element)
                
    @staticmethod
    def project_image(
            k, 
            elements, 
            projection_type
            ):
        """
        Static method which projects
        a digital image.
        
        Parameters:
            k: int.
                Initial subdivision which 
                is considered.
            elements: List of tuples.
                Elements to map.
            projection_type: str.
                Type of projection selected.
                It can be canonical or partial.
                    
        Returns:
            new_elements: List of tuples.
                projections of original elements.
        """
        new_elements = []
        for element in elements:
            if projection_type in ['canonical', 'partial']:
                new_element = tuple(__class__.project_element(
                    k, 
                    element, 
                    projection_type
                    ))
            else: 
                print('This projection type is not contempled.')
                return None
            if new_element not in new_elements:
                new_elements.append(new_element)
        return new_elements
    
    @staticmethod
    def image_product(
            elements_image_1, 
            elements_image_2
            ):
        """
        Static method which calculates digital
        product.

        Parameters:
            elements_image_1 : List of tuples.
                List of elements.
            elements_image_2 : List of tuples.
                List of elements.
        
        Returns:
            new_elements: List of tuples.
                List of elements which is the
                product.
            
        """
        new_elements = []
        for element in itertools.product(*[elements_image_1, elements_image_2]):
            new_element = []
            for n in range(2):
                for coordinate in element[n]:
                    new_element.append(coordinate)
            new_elements.append(tuple(new_element))
        return new_elements
        
        
    @staticmethod 
    def plot_digital_image(elements):
        """
        Static method which plots a digital
        image.

        Parameters:
            elements : List of tuples.
                List of elements which are going
                to be plotted.
        
        Returns:
            None.
            
        """
        dimension = len(elements[0])
        if dimension == 1:
            new_elements = []
            for element in elements:
                new_elements.append((element[0],0))
            __class__.plot_digital_image(new_elements)
        elif dimension == 2:
            x,y = zip(*elements)   
            fig = plt.figure()
            ax = fig.gca()
            ax.scatter(x, y)
            plt.title('Digital image plot.')
        elif dimension == 3:
            x,y,z = zip(*elements)   
            fig = plt.figure()
            ax = fig.gca(projection='3d')
            ax.scatter(x, y, z)
            plt.title('Digital image plot.')
        else:
            print('A plot cannot be done in higher dimensions than 3')
            

        
if __name__ == '__main__':
    
    #We declare our digital images examples
    I4 = digital_image(None, 'I4')
    I3 = digital_image(None, 'I3')
    #We extract elements of I3 and I4
    I3_elements = list(I3.elements.keys())
    I4_elements = list(I4.elements.keys())
    #We show dictionary of adjacent elements in I3
    print(I3.elements)
    """
    Output: {(0,): [(1,)], (1,): [(0,), (2,)], (2,): [(1,), (3,)], (3,): [(2,)]}
    """
    #We calculate the third subdivision of I3 i.e. I11
    print(I3.subdivision(3,  I3_elements))
    """
    Output: [(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), (11,)]
    """
    #We calculate partial projection of previous i.e. I7
    print(I3.project_image(
            3, 
            I3.subdivision(3,  I3_elements), 
            'partial'
            ))
    """
    Output: [(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,)]
    """
    #We calculate canonical projection of previous i.e. I3
    print(I3.project_image(
            3, 
            I3.subdivision(3,  I3_elements), 
            'canonical'
            ))
    """
    Output: [(0,), (1,), (2,), (3,)]
    """
    #We calculate I4 x I3 and plot it
    d = digital_image(None, None)
    product = d.image_product(
        I4_elements,
        I3_elements
        )
    print(product)
    """
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), 
     (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), 
     (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), 
     (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)]
    """
    d.plot_digital_image(product)
    
    
    
        