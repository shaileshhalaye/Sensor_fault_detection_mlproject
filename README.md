git add README.md
Project overview
Why sensor fault detection?
Company name: XYZ

Company producing: Vehicle

Engineering Team preparing: APS (Air pressure System)

APS application: Braking system

In case of failure we have to identify whether the failure is because of APS or not.

APS: It contains sensors, almost 170 nos, 

Input :  Readings of a sensor:havve to decide wether it because of sensor or not. 

Outut  :  Yes or No.

Dataset : Historical readings of sensors, Labels: Yes or No

S1   S2 ......S170     Class
0.3  0.4       0.6       Yes

# Requirement

1. Failure reason-----> is is because of APS or not

We will use ML technic to solve this problem

How we can use ML here.

1. We need historical data

  readings of sensors along with labels. Using readings of sensors helps us to identify wether failure within APS or not.


# Prerequisite
1. MONGODB: Available in MONGO DB
2. ML algorithm with some lib such scikit, pandas, and numpy to understand the programe. 
3. Basic cloud knowledge such as VM, Storage Service
4. SCM (Source control management tools) such as git, github. 

Existing Solutions:

Mechanic will investigate physically and they will try to confirm if failure is in APS or not.

Problems:
1. Cost
2. Time

Some times failure is not because of APS then also you have to go for routine checkup for APS systems. 

What benefit you will get.

1. Instance notification if failure is there because software can be installed in vehical.
2. User will know in advance there is failure in APS.
3. Schedule a time to repair your car


