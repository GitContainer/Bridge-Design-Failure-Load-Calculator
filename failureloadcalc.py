#CIV102 Matboard Bridge Design Project: Failure Loads Under Baldwin Loading
#As part of the Structures and Materials course of the Engineering Science Program at the University of Toronto,the Matboard Bridge Design Project challenges students to design a bridge that can resists a force upwards of 400 Newton under 2 different types of loading. However, this program is only applicable to loading under the Baldwin Universal Testing Machine. Using different concepts and equations taught throughout the course, students must calculate all possible failure method of their bridge and predict ultimately what load will cause their bridge to fail. Such concepts include drawing and reading Shear Force and Bending Moment diagrams, using Jourawski's equation, applying the knowledge of thin plate buckling, etc. Once the design is finalized, students must construct the bridge using the provided limited materials:1 sheet of matboard and 2 tubes of contact cement glue. After the construction of the bridge, it is then tested in a lab under a train loading and the Baldwin loading. The more force the bridge is able to resist is desired.

#basic helper functions
def square(n):
   return n*n

def cube(n):
   return n*n*n

#try except helper function that will reduce repetitiveness in code when checking if user input is valid
def try_except(n,errormessage,message):
   break_loop=False
   while break_loop==False:
      try:
         #the goal is to convert the user input into a float, which can then be used to compute various failure loads
         #firstly, need to check if the input value is valid to convert into a float type, if not, the except loop will be executed
         float(n)
         #convert user input value into float
         n=float(n)
         #user input is now converted into a float, the while loop can now be broken
         break_loop=True
      except:
         #error message indicating that the user did not input valid values
         print(errormessage)
         #asks user to input valid input once again
         n=input(message)
   return n 

#class begins
class failure:
   def __init__(self):
      #creating constants that will be calculated later by the methods below. Constants include: the Second Moment of Inertia, the centroidal axis from the bottom, the centroidal axis from the top, the First Moment of Inertia of the cross section, and the First Moment of Inertia of the glue.
      self.I=0
      self.ybot=0
      self.ytop=0
      self.Qshear=0
      self.Qglue=0
      #initializing constants given by the project instructions
      self.stress_comp=6
      self.stress_tensile=30
      self.T_matboard=4
      self.T_glue=2
      self.young_modulus=4000
      self.poisson=0.2

#finding of centroidal axis: The centroidal axis is the quotient of the sums of the product of the area of each section and the respective centroidal axis of that section and the sum of the areas of each sections. The mathematical equation can be given by: (A1y1+A2y2...An-1yn-1+Anyn)/(A1+A2+...An-1An), where A is the area of each section and y is the respective centroidal axis of each section.
   def y(self):
      #accum will be the sum of the numerator, (A1y1+A2y2...An-1yn-1+Anyn)
      accum=0
      #area_sum will be the sum of the denominator, or the sum of all the areas of each section (A1+A2+...An-1An)
      area_sum=0
      #a counter will keep track of the additiong of each sections present in the cross section
      cnt=0
      #user will need to specify how many sections are present in the cross sections
      n=input("Enter the number of sections in the cross section:")
      #check and convert the user inputed value into a float
      n=try_except(n,"Error the number of sections you have entered is not a number","Enter the number of sections in the cross section:")
      while cnt<n:
         #need the value of the base for area calculations
         b=input("Enter the dimension of the base of the section:")
         #error check if user input is valid
         b=try_except(b,"Error, the base you have entered is not a number","Enter the dimension of the base of the section:")
         #need the value of the height for area calculations as well       
         h=input("Enter the dimension of the height of the section:")
         #error check if user input is valid
         h=try_except(h,"Error, the height you have entered is not a number","Enter the dimension of the height of the section:")
         #need the value of the respective centroidal axis of each section         
         ybar=input("Enter the distance from the centroidal axis of the section to the bottom of the cross section:")
         #error check if user input is valid
         ybar=try_except(ybar,"Error, the distance from the centroidal axis of the section to the bottom of the cross section you have entered is not a number", "Enter the distance from the centroidal axis of the section to the bottom of the cross section:")
         #calculation of area for the respective section        
         area=b*h
         #summing numerator
         accum=accum+(area*ybar)
         #summing denominator
         area_sum=area_sum+area
         #increase counter for next section in the cross section
         cnt=cnt+1
      #need the value of the total height of the cross section to determine the centroidal axis from the top and from the bottom
      height=input("Enter the total height of the cross section:")
      #error check if user input is valid
      height=try_except(height,"Error, the total height you have entered is not a number", "Enter the total height of the cross section:")
      #computation of centroidal axis from the bottom and then storing it in the constant that was initialized to 0
      self.ybot=accum/area_sum
      print("ybot="+str(self.ybot))
      #computation of centroidal axis from the top and then storing it in the constant that was initialized to 0
      self.ytop=height-self.ybot
      print("ytop="+str(self.ytop))
      return True

#finding of Second Moment of Inertia: The total Second Moment of Inertia (I) can be found by summing each individual I of each individual section of the cross section. I can be found by using the Parallel Axis Theorem, described by the equation (bh^3/12)+b*h*(y-ybar)^2, where b is the base of the individual section, h is the height of the section, y is the centroidal axis from the bottom, and ybar is the respective centroidal axis of the section.
   def second_moment_of_inertia(self):
      #accum will be the sum of the Is of each individual section of the cross section
      accum=0
      #a counter will keep track of the additiong of each sections present in the cross section
      cnt=0
      #user will need to specify how many sections are present in the cross sections
      n=input("Enter the number of sections in the cross section:")
      #error check if user input is valid
      n=try_except(n,"Error the number of sections you have entered is not a number","Enter the number of sections in the cross section:")
      while cnt<n:
         #need the value of the base
         b=input("Enter the dimension of the base of the section:")
         #error check if user input is valid
         b=try_except(b,"Error, the base you have entered is not a number","Enter the dimension of the base of the section:")
         #need the value of the height
         h=input("Enter the dimension of the height of the section:")
         #error check if user input is valid
         h=try_except(h,"Error, the height you have entered is not a number","Enter the dimension of the height of the section:")
         ybar=input("Enter the distance from the centroidal axis of the section to the bottom of the cross section:")
         #error check if user input is valid
         ybar=try_except(ybar,"Error, the distance from the centroidal axis of the section to the bottom of the cross section you have entered is not a number", "Enter the distance from the centroidal axis of the section to the bottom of the cross section:") 
         #computation of area of section
         area=b*h
         #computation of the first part of the Parallel Axis Theorem
         first=(b*cube(h))/12
         #computation of the distance between the centroidal axis and the centroidal axis of the respective section
         distance=square(ybar-self.ybot)
         #computation of the Second Moment of Inertia
         moment=first+(area*distance)
         #summing of idividual Is
         accum=accum+moment
         #increase counter for next section in cross section
         cnt=cnt+1
      #set the internal variable of I to the calculated value
      self.I=accum
      print("I="+str(self.I))
      return True


#finding of First Moment of Inertia for Matboard: The total First Moment of Inertia (Q) can be found by summing each individual Q of each individual section of the cross section. Q can be found by multiplying the area of the individual section by the distance between the respective centroidal axis of the section and the centroidal axis of the cross section.
   def Q_shear(self):
      accum=0
      cnt=0
      #user will need to specify how many sections are present in the cross sections
      n=input("Enter the number of sections in the cross section:")
      #error check if user input is valid
      n=try_except(n,"Error the number of sections you have entered is not a number","Enter the number of sections in the cross section:")
      while cnt<n:
         #need the value of the base for area calculations
         b=input("Enter the dimension of the base of the section:")
         #error check if user input is valid
         b=try_except(b,"Error, the base you have entered is not a number","Enter the dimension of the base of the section:")
         #need the value of the height for area calculations
         h=input("Enter the dimension of the height of the section:")
         #error check if user input is valid
         h=try_except(h,"Error, the height you have entered is not a number","Enter the dimension of the height of the section:") 
         #need the distance between centroidal axes for first moment of area calculations 
         distance=input("Enter the distance from the centroidal axis of the section to the centroidal axis:")
         #error check if user input is valid 
         distance=try_except(distance, "Error, the distance you have entered is not a number", "Enter the distance from the centroidal axis of the section to the centroidal axis:")
         #computation of area of section
         area=b*h
         #computation of the First Moment of Inertia
         Q=area*distance
         #summing of idividual Qs
         accum=accum+Q
         #increase counter for next section in cross section
         cnt=cnt+1
      #set the internal variable of Qshear to the calculated value
      self.Qshear=accum
      print("Qshear=" + str(self.Qshear))
      return True


#finding of First Moment of Inertia for Glue: Identical process to finding the First Moment of Inertia for the Matboard
   def Q_glue(self):
      accum=0
      cnt=0
      #user will need to specify how many sections are present in the cross sections
      n=input("Enter the number of sections in the cross section:")
      #error check if user input is valid
      n=try_except(n,"Error the number of sections you have entered is not a number","Enter the number of sections in the cross section:")
      while cnt<n:
         #need the value of the base for area calculations
         b=input("Enter the dimension of the base of the section:")
         #error check if user input is valid
         b=try_except(b,"Error, the base you have entered is not a number","Enter the dimension of the base of the section:")
         #need the value of the height for area calculations
         h=input("Enter the dimension of the height of the section:")
         #error check if user input is valid
         h=try_except(h,"Error, the height you have entered is not a number","Enter the dimension of the height of the section:")
         #need the distance between centroidal axes for first moment of area calculations 
         distance=input("Enter the distance from the centroidal axis of the section to the centroidal axis:")
         #error check if user input is valid 
         distance=try_except(distance, "Error, the distance you have entered is not a number", "Enter the distance from the centroidal axis of the section to the centroidal axis:")
         #computation of area of section
         area=b*h
         #computation of the First Moment of Inertia
         Q=area*distance
         #summing of idividual Qs
         accum=accum+Q
         #increase counter for next section in cross section
         cnt=cnt+1
      #set the internal variable of Qglue to the calculated value
      self.Qglue=accum
      print("Qglue=" +str(self.Qglue))
      return True

#crushing failure: To determine the crushing failure load, one must use Navier's equation (stress=(moment*centroidal axis)/second moment of inertia). Since moment will be in terms of failure load, one must rearrange for moment. Moment is read from the Bending Moment diagram.
   def crush(self):
      print("You are now calculating for the crushing failure load")
      #getting the value of the moment
      moment=input("Enter the Moment in terms of failure load:")
      #error check if user input is valid
      moment=try_except(moment,"Error, the Moment you have entered is not a number","Enter the Moment in terms of failure load:")
      #one must 
      y=input("Enter if calculating using ytop or ybot:")
      #error check if user input is valid
      while y!="ytop" and y!="ybot":
         print("Error, did not enter ytop or ybot")
         y=input("Enter if calculating using ytop or ybot:")
      if y=="ytop":
         #computation of crushing failure load using the rearranged from of Navier's equation, substituting in the value of user inputed moment value and ytop 
         p=(self.I*self.stress_comp)/(moment*self.ytop)
      elif y=="ybot":
         #computation of crushing failure load using the rearranged from of Navier's equation, substituting in the value of user inputed moment value and ybot
         p=(self.I*self.stress_comp)/(moment*self.ybot)
      print("The crushing failure load is" + str(p))
      return True

#tension failure: This process is identically to crushing failure except the value of the stress used is different (30MPa instead of 6MPa).
   def tensile(self):
      print("You are now calculating for the tensile failure load")
      #getting the value of the moment
      moment=input("Enter the Moment in terms of failure load:")
      #error check if user input is valid
      moment=try_except(moment,"Error, the Moment you have entered is not a number", "Enter the Moment in terms of failure load:")
      y=input("Enter if calculating using ytop or ybot:")
      #error check if user input is valid
      while y!="ytop" and y!="ybot":
         print("Error, did not enter ytop or ybot")
         y=input("Enter if calculating using ytop or ybot:")
      if y=="ytop":
         #computation of crushing failure load using the rearranged from of Navier's equation, substituting in the value of user inputed moment value and ytop 
         p=(self.I*self.stress_tensile)/(moment*self.ytop)
      elif y=="ybot":
         #computation of crushing failure load using the rearranged from of Navier's equation, substituting in the value of user inputed moment value and ybot
         p=(self.I*self.stress_tensile)/(moment*self.ybot)
      print("The tensile failure load is" +str(p))
      return True

#Matboard shear failure: To determine the Matboard shear failure load, one must use Jourawski's equation (Force=(Shear force*First Moment of Inertia)/Second Moment of Inertia*base). Since shear force  will be in terms of failure load, one must rearrange for the shear force. Shear force is read from the Shear Force diagram at the maximum point.
   def shear(self):
      print("You are now calculating for the matboard shear failure load")
      #need the value of the base to use Jourawski's equation
      base=input("Enter the dimension of the base:")
      #error check if user input is valid
      base=try_except(base,"Error, the base you have entered is not a number","Enter the dimension of the base:")
      #need the value of the Shear Force according to the Shear Force diagram to use Jourawski's equation
      V=input("Enter the Shear Force in terms of failure load:")
      #error check if user input is valid
      V=try_except(V,"Error, the Shear Force you have entered is not a number", "Enter the Shear Force in terms of failure load:")
      #computation of matboard shear failure load
      p=(self.I*base*self.T_matboard)/(self.Qshear*V)
      print("The shear failure load for the matboard is" + str(p))
      return True

#Glue shear failure:This process is identically to crushing failure except the First Moment of Inertia is different for the glue (use Qglue instead of Qshear)
   def glue_shear(self):
      print("You are now calculating for the glue shear failure load")
      #need the value of the base to use Jourawski's equation
      base=input("Enter dimension of the base:")
      #error check if user input is valid
      base=try_except(base,"Error, the base you have entered is not a number","Enter the dimension of the base:")
      #need the value of the Shear Force according to the Shear Force diagram to use Jourawski's equation
      V=input("Enter the Shear Force in terms of failure load:")
      #error check if user input is valid
      V=try_except(V,"Error, the Shear Force you have entered is not a number", "Enter the Shear Force in terms of failure load:")
      #computation of glue shear failure load
      p=(self.I*base*self.T_glue)/(self.Qglue*V)
      print("The shear failure load for the glue is" + str(p))
      return True

#plate buckling
#2 fixed ends: To determine the plate buckling failure load with 2 fixed ends, one must use the plate buckling equation [((4*pi^2*young's modulus)/(12*(1-poisson's variable^2)))*(t/b)^2, where t is the thickness and b is the base] and compare it to the stress calculated by using Navier's equation. 
   def two_fix(self):
      print("You are now calculating for the thin plate buckling failure load with 2 fixed ends")
      #need the thickness to use plate buckling equation
      t=input("Enter the dimension of the thickness:")
      #error check if user input is valid
      t=try_except(t,"Error, the thickness you have entered is not a number", "Enter the dimension of the thickness:")
      #need the base to use plate buckling equation
      b=input("Enter dimension of the base:")
      #error check if user input is valid
      b=try_except(b,"Error, the base you have entered is not a number", "Enter the dimension of the base:")
      #getting the value of the moment based on the Bending Moment diagram at the appropriate point to use in the plate buckling equation
      moment=input("Enter the Moment in terms of failure load:")
      #error check if user input is valid
      moment=try_except(moment,"Error, the Moment you have entered is not a number", "Enter the Moment in terms of failure load:")
      y=input("Enter if calculating using ytop or ybot:")
      #error check if user input is valid
      while y!="ytop" and y!="ybot":
         print("Error, did not enter ytop or ybot")
         y=input("Enter if calculating using ytop or ybot:")
      if y=="ytop":
         #computation of the stress using Navier's equation, substituting ytop
         stress=(moment*self.ytop)/self.I
      elif y=="ybot":
         #computation of the stress using Navier's equation, substituting ytop
         stress=(moment*self.ybot)/self.I
      stresscrit=((4*square(3.141592653589793)*self.young_modulus)/(12*(1-square(self.poisson))))*(square(t/b))
      #computation of the failure load by dividing the critical stress by the stress calculated using Navier's equation
      p=stresscrit/stress
      print("The thin plate buckling failure load with 2 fixed ends is" + str(p))
      return True

#1 free edge:This process is identically to the 2 fixed end calculations except different dimension values (ex: base value) are used and the plate buckling equation is slightly different, multiplying by 0.425 instead of 4. 
   def free_edge(self):
      print("You are now calculating for the thin plate buckling failure load with 1 free edge")
      #need the thickness to use plate buckling equation
      t=input("Enter the dimension of the thickness:")
      #error check if user input is valid
      t=try_except(t,"Error, the thickness you have entered is not a number", "Enter the dimension of the thickness:")
      #need the thickness to use plate buckling equation
      b=input("Enter dimension of the base:")
      #error check if user input is valid
      b=try_except(b,"Error, the base you have entered is not a number", "Enter the dimension of the base:")
      #getting the value of the moment based on the Bending Moment diagram at the appropriate point to use in the plate buckling equation
      moment=input("Enter the Moment in terms of failure load:")
      #error check if user input is valid
      moment=try_except(moment,"Error, the Moment you have entered is not a number", "Enter the Moment in terms of failure load:")
      y=input("Enter if calculating using ytop or ybot:")
      #error check if user input is valid
      while y!="ytop" and y!="ybot":
         print("Error, did not enter ytop or ybot")
         y=input("Enter if calculating using ytop or ybot:")
      if y=="ytop":
         #computation of the stress using Navier's equation, substituting ytop
         stress=(moment*self.ytop)/self.I
      elif y=="ybot":
         #computation of the stress using Navier's equation, substituting ybot
         stress=(moment*self.ybot)/self.I
      stresscrit=((0.425*square(3.141592653589793)*self.young_modulus)/(12*(1-square(self.poisson))))*(square(t/b))
      #computation of the failure load by dividing the critical stress by the stress calculated using Navier's equation
      p=stresscrit/stress
      print("The thin plate buckling failure load with 1 free edge is" +str(p))
      return True


#web buckling: Again, this process is identically to the 2 fixed end calculations except different dimension values (ex: base value) are used and the plate buckling equation is slightly different, multiplying by 6 instead of 4. 
   def web_buckling(self):
      print("You are now calculating for the web buckling failure load")
      #need the thickness to use plate buckling equation
      t=input("Enter the dimension of the thickness:")
      #error check if user input is valid
      t=try_except(t,"Error, the thickness you have entered is not a number", "Enter the dimension of the thickness:")
      #need the thickness to use plate buckling equation
      b=input("Enter dimension of the base:")
      #error check if user input is valid
      b=try_except(b,"Error, the base you have entered is not a number", "Enter the dimension of the base:")
      #getting the value of the moment based on the Bending Moment diagram at the appropriate point to use in the plate buckling equation
      moment=input("Enter the Moment in terms of failure load:")
      #error check if user input is valid
      moment=try_except(moment,"Error, the Moment you have entered is not a number", "Enter the Moment in terms of failure load:")
      y=input("Enter if calculating using ytop or ybot:")
      #error check if user input is valid
      while y!="ytop" and y!="ybot":
         print("Error, did not enter ytop or ybot")
         y=input("Enter if calculating using ytop or ybot:")
      if y=="ytop":
         #computation of the stress using Navier's equation, substituting ytop
         stress=(moment*self.ytop)/self.I
      elif y=="ybot":
         #computation of the stress using Navier's equation, substituting ybot
         stress=(moment*self.ybot)/self.I
      #computation of the critical stress using the plate buckling equation
      stresscrit=((6*square(3.141592653589793)*self.young_modulus)/(12*(1-square(self.poisson))))*(square(t/b))
      #computation of the failure load by dividing the critical stress by the stress calculated using Navier's equation
      p=stresscrit/stress
      print("The web buckling failure load is" +str(p))
      return True

#diaphragm shear: Once again, this process is very similar to the 2 fixed end calculations except different dimension values (ex: base value) are used, additional dimension values are needed such as the spacing between each diaphragm, and the plate buckling equation is different. The plate buckling equation used to find the critical Shear Force is instead ((5*pi^2*Young's Modulus)/(12*(1-poisson's variable^2)))*((t/a)^2+(t/h)^2), where a is the spacing between diaphragms. 
   def diashear(self):
      print("You are now calculating for the diaphragm shear failure load")
      #need the thickness to use diaphragm shear equation
      t=input("Enter the dimension of the thickness:")
      #error check if user input is valid
      t=try_except(t,"Error, the thickness you have entered is not a number", "Enter the dimension of the thickness:")
      #need the thickness to use diaphragm shear equation
      b=input("Enter dimension of the base:")
      #error check if user input is valid
      b=try_except(b,"Error, the base you have entered is not a number", "Enter the dimension of the base:")
      #need the height to use diaphragm shear equation
      h=input("Enter the height:")
      #error check if user input is valid
      h=try_except(h,"Error, the height you have entered is not a number", "Enter the height:")
      #need the spacing between diaphragms to use diaphragm shear equation
      a=input("Enter the spacing between diaphragms:")
      #error check if user input is valid
      a=try_except(a,"Error, the spacing you have entered is not a number","Enter the spacing between diaphragms:")
      V=input("Enter the Shear Force in terms of failure load:")
      #error check if user input is valid
      V=try_except(V,"Error, the Shear Force you have entered is not a number", "Enter the Shear Force in terms of failure load:")
      Tcrit=((5*square(3.141592653589793)*self.young_modulus)/(12*(1-square(self.poisson))))*(square(t/a)+square(t/h))
      p=(Tcrit*self.I*b)/(self.Qshear*V)
      print("The diaphragm shear failure load is" + str(p))
      return True
