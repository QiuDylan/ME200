# Assessing a 2015 Toyota Camry Windshield Wiper System
# Final project of ME200, Fall 2024 semester: Dylan Qiu, Ishaan Zaveri, Sadia Rahman

### Version Control: 
```
python min = 3.10.0
numpy = 1.26 < x < 1.29
scipy = 1.14.1
pandas = 2.2.3
matplotlib = 3.9.3
```
### Execution:
Start by running *FinalProj/4B_Mechanism.ipynb*, make sure to follow every block individually instead of doing *run all*. Use the following values for the initial **R2, initial angle = 270, inital angular velocity = 6.81 rad/s**. <br>
After running that, execute *FinalProj/Final_Project_V3_JNotebook.ipynb* to get the acceleration plots. 

### Introduction:
    Introduction
        This project aims to understand the dynamics of a windshield wiper system by creating a model that will take an input torque and assess the output normal force. Stemming from an interest in automobiles due to our collective participation in motorsports, we aimed to assess the windshield wiper system that identified with the knowledge we have on four bar linkages. To do this, we assessed the fastest speed of the windshield wipers on a 2015 Toyota Camry LE. Using Tracker, we obtained data for the position, velocity, and acceleration of windshield wiper. This was used to confirm our model made using Python.
### Assumptions:
    Assumptions and Approach 
        Throughout the experiment many assumptions were made to minimize the number of unknowns and simplify the system. To begin with, we assessed the system on a plane horizontal to the force of gravity. Through this we assumed there was some moment of inertia, mass, and length of the wiper that we can be held constant. We set the wiper to be a singular rigid body that has an unknown constant force of friction acting perpendicular to the motion. These simplifications allowed us to assess the same system but at the angle of the windshield, where we know there is a component of some unknown constant normal force. Gravity was set to 9.81 m/s2. The car remained indoors throughout the whole process to minimize the effect of outside elements such as wind. It was assumed that the motor had no angular acceleration. 
        Before starting the experiment, we came up with an initial FBD utilizing a simple windshield model [1] as shown in Figure 1. We then determined the FBD and KD for the singular wiper as shown in Figure 2.
    Figure 1: FBD of Windshield Wiper System
    
    <insert image here>
    
    
    
    
    
    
    
    
    
    
    We utilized Figure 2 to come up with our basic equations of motion (Figure 3) by setting 
    up the force equations in the x and y direction and the moment of point G. This was done for the flat plane and angled plane case. 
    
### Methods:
    Methods 
        The surface of the windshield was cleaned and dried to ensure no debris would affect our data. We measured the windshield arm, Link AB and CD (Figure 1) using a measuring tape. Figure 4 was used to find the values for the other linkages by drawing lines and using ratios. The angle of the windshield was measured using an online protractor. 
        The car was then turned on with one wiper propped up. We primarily wanted to model one as they each would have the same movements. A piece of white tape was placed at the middle of the windshield wiper, this was our point C (Figure 1). The wiper was set to its highest setting for ten cycles. This was recorded to put into Tracker where the white tape was tracked through 3 cycles. Using the data from Tracker we constructed plots of the speeds and accelerations.
    Figure 4: Windshield Wiper System of a 2015 Toyota Camry
       <insert figure here>
    Figure 5: Velocity [Left] and Acceleration [Right] of Four Bar Linkage [2] 
        Using python, we performed positional, velocity, and acceleration analysis using the measured lengths to create datasets. Grashof’s Law was used to define this linkage as a Crank and Rocker Mechanism and then Figure 5 was used to calculate the angles for our calculations. A dataset was created containing the angular position, velocity, and acceleration of each member of the four-bar. We used these datasets of data to generate plots of the members and generate a visual simulation of the four-bar linkage under the hood.
        Using the dataset, we performed torque calculations to find the torque on the center of mass of the wiper. We then used the equations of motions to solve for the tangential and normal accelerations, the normal force, and the friction force. To obtain the velocity and position we integrated the acceleration values using trapezoidal rule. We then plotted the graphs of position, tangential velocity, tangential acceleration, torque, normal force, friction force, and spring force based on time. The torque graph required a Savizky filter due to the asymptotes.
    
### Discussion:
    Discussion 
        This experiment helped us model the effect of two different input speeds on the force of friction and normal force applied onto a windshield wiper at a range of times. There were many outside factors that contributed to the error in our data. To begin with, our method of measuring the linkages was heavily approximated. In addition, the wiper conditions could have heavily played in its functioning. The Camry, before experimentation, had not used its wipers in over 6 months. Some rusting of the bolts due to the dark, moist conditions of the garage could have factored in as well.
        In the future, error can be minimized by using a new system and opening the panels to see the whole mechanism working. In addition, many assumptions were made to simplify the system that could have influenced the results. The results of the model was higher in all aspects compared to the collected tracker data as shown in the plots. This is most likely due to the different forms of error that lowered the overall output torque and speed/acceleration of the windshield wiper arm. The friction force, normal force, and spring force graphs look fairly accurate and the first two are related by a factor of 0.3 due to the coefficient of kinetic friction. This is most likely also affected by the difference in wiper and glass combinations that the Toyota Camry had in comparison to the one used in the study. These graphs can’t be compared to a real value that is tested. The velocity and position graphs were obtained through integration and the first peak of both graphs are correct but there is some sort of drift affecting the rest of the graph that can’t be solved for. The tangential acceleration plot which is one of the unknowns we solved for with our system is very similar to the tracker plot which supports the validity of the model. Overall, this model has produced an ideal simulation of a windshield wiper system.
### Bibliography:
    [1]	Skyline Tutorials, How Quick Return Mechanism Work! |Best 3D Animation| Crank & Slotted lever or Whitworth Mechanism|, (Oct. 24, 2015). Accessed: Dec. 08, 2024. [Online Video]. Available: [link](https://www.youtube.com/watch?v=s3G3au-EyAQ)
    [2]	“4bar_mechanism/Images/4Bar.png at main · alejo1630/4bar_mechanism,” GitHub. Accessed: Dec. 10, 2024. [Online]. Available: [link](https://github.com/alejo1630/4bar_mechanism/blob/main/Images/4Bar.png)
    [3]	admin@showsenmoto.com, “Wiper Motor FAQ in 2020 - Everything About Windshield Wiper Motor,” SHOWSEN®. Accessed: Dec. 08, 2024. [Online]. Available: [link](https://showsenmoto.com/wiper-motor-faqs/)
    [4]		Bódai, G., Goda, T.J. Friction Force Measurement at Windscreen Wiper/Glass Contact. Tribol Lett 45, 515–523 (2012). [link](https://doi.org/10.1007/s11249-011-9907-2)
    
    