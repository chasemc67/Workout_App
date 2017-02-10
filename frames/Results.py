import tkinter as tk   # python3

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

from Database.DB import insertPerson

from pdf.generatePdf import *

class Results(tk.Frame):

   def savePerson(self):
    try:
     dbID = getattr(self.controller.person, "dbID")
     return
     # update entry instead of adding new person     
    except:
     insertPerson(self.controller.person)
    
   def printPerson(self):


   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.person = self.controller.person

   def showBMIresult(self, person):
       self.BMIresult = tk.Label(self)
       self.BMIresult["text"] = ("BMI: " + str(person.getBMI()))
       self.BMIresult.pack()

   def showCircumferenceResult(self, person):

       if person.hipCirc != "\n":
        self.hipCircLabel = tk.Label(self)
        self.hipCircLabel["text"] = ("Hip Circumference(cm): " + self.person.hipCirc)
        self.hipCircLabel.pack()
        self.hipCircValue = tk.Label(self)
        self.hipCircValue["text"] = person.hipCirc
        self.hipCircValue.pack()

       if person.waistCirc != "\n":
        self.waistCircLabel = tk.Label(self)
        self.waistCircLabel["text"] = ("Waist Circumference(cm): " + self.person.waistCirc)
        self.waistCircLabel.pack()

       if person.armCirc != "\n":
        self.armCircLabel = tk.Label(self)
        self.armCircLabel["text"] = ("Arm Circumference(cm): " + self.person.armCirc)
        self.armCircLabel.pack()

       if person.thighCirc != "\n":
        self.thighCircLabel = tk.Label(self)
        self.thighCircLabel["text"] = ("Thigh Circumference(cm): " + self.person.thighCirc)
        self.thighCircLabel.pack()

       if person.chestCirc != "\n":
        self.chestCircLabel = tk.Label(self)
        self.chestCircLabel["text"] = ("Chest Circumference(cm): " + self.person.chestCirc)
        self.chestCircLabel.pack()

   def showThreeSiteSkinfoldResult(self, person):
      if (person.threeSiteFemaleSupra != "\n" and person.threeSiteFemaleTricep != "\n" and person.threeSiteFemaleThigh != "\n"):
       self.threeSiteBDMaleLabel = tk.Label(self)
       self.threeSiteBDMaleLabel["text"] = ("Body Density: " + str(person.getThreeSiteMale()))
       self.threeSiteBDMaleLabel.pack()

       self.threeSiteBFMaleLabel = tk.Label(self)
       self.threeSiteBFMaleLabel["text"] = ("Body Fat %: " + str(person.getBodyFatThreeMale()))
       self.threeSiteBFMaleLabel.pack()

      if (person.threeSiteMaleChest != "\n" and person.threeSiteMaleAb != "\n" and person.threeSiteMaleThigh != "\n"):
        self.threeSiteBDFemaleLabel = tk.Label(self)
        self.threeSiteBDFemaleLabel["text"] = ("Body Density: " + str(person.getThreeSiteFemale()))
        self.threeSiteBDFemaleLabel.pack()

        self.threeSiteBFFemaleLabel = tk.Label(self)
        self.threeSiteBFFemaleLabel["text"] = ("Body Fat %: " + str(person.getBodyFatThreeFemale()))
        self.threeSiteBFFemaleLabel.pack()

   def showSvnSiteSkinfoldResult(self, person):
       self.SvnSiteBDLabel = tk.Label(self)
       self.SvnSiteBDLabel["text"] = ("Body Density: " + str(person.getSevenSiteDensity()))
       self.SvnSiteBDLabel.pack()

       self.SvnSiteBFLabel = tk.Label(self)
       self.SvnSiteBFLabel["text"] = ("Body Fat %: " + str(person.getBodyFatSeven()))
       self.SvnSiteBFLabel.pack()

   def showModAstResult(self, person):
       self.ModAstCapacityLabel = tk.Label(self)
       self.ModAstCapacityLabel["text"] = ("Test: Modified Astrand Cycle Test VO2max(ml/kg/min): " + self.person.modAstAerobic)
       self.ModAstCapacityLabel.pack()

   def showEbbelingResult(self, person):
       self.EbbelingCapacityLabel = tk.Label(self)
       self.EbbelingCapacityLabel["text"] = ("Test: Ebbeling Treadmill Test VO2max(ml/kg/min): " + str(person.getEbellingAerobic()))
       self.EbbelingCapacityLabel.pack()

   def showRockportResult(self, person):
       self.RockportCapacityLabel = tk.Label(self)
       self.RockportCapacityLabel["text"] = ("Test: Rockport 1 Mile Walk VO2max(ml/kg/min): " + str(person.getRockportAerobic()))
       self.RockportCapacityLabel.pack()

   def showCoopersResult(self, person):
       self.CoopersCapacityLabel = tk.Label(self)
       self.CoopersCapacityLabel["text"] = ("Test: Coopers Run Test VO2max(ml/kg/min): " + str(person.getCooperAerobic()))
       self.CoopersCapacityLabel.pack()

   def showMBTossResult(self, person):
       self.MBTossLabel = tk.Label(self)
       self.MBTossLabel["text"] = "Med. Ball Toss"
       self.MBTossLabel.pack()

       self.MBTossDistLabel = tk.Label(self)
       self.MBTossDistLabel["text"] = ("Throw Distance(cm): " + self.person.seatMBDist)
       self.MBTossDistLabel.pack()

   def showVertJumpResult(self, person):
        self.vertJumpLabel = tk.Label(self)
        self.vertJumpLabel["text"] = "Vertical Jump"
        self.vertJumpLabel.pack()

        self.vertJumpReachLabel = tk.Label(self)
        self.vertJumpReachLabel['text'] = ("Reach: " + self.person.vertJumpSR)
        self.vertJumpReachLabel.pack()

        self.vertJumpCalcOutputLabel = tk.Label(self)
        self.vertJumpCalcOutputLabel['text'] = "Calc output: " + str(person.getVertJumpBest())
        self.vertJumpCalcOutputLabel.pack()

        self.vertJumpPowerLabel = tk.Label(self)
        self.vertJumpPowerLabel["text"] = ("Peak Power(W):" + str(person.getVertJumpPower()))
        self.vertJumpPowerLabel.pack()

   def showRMTestResult(self, person):
       self.RMTestResultLabel = tk.Label(self)
       self.RMTestResultLabel["text"] = "1RM Test"
       self.RMTestResultLabel.pack()

       if (person.RMTestExA != "\n" and person.RMTestExAWeight != "\n"):
        self.RMTestExALabel = tk.Label(self)
        self.RMTestExALabel["text"] = ("Exercise: " + self.person.RMTestExA)
        self.RMTestExALabel.pack()

        self.RMTestExAWeightLabel = tk.Label(self)
        self.RMTestExAWeightLabel["text"] = ("1 Rep Max: " + self.person.RMTestExAWeight)
        self.RMTestExAWeightLabel.pack()

       if (person.RMTestExB != "\n" and person.RMTestExBWeight != "\n"):
        self.RMTestExBLabel = tk.Label(self)
        self.RMTestExBLabel["text"] = ("Exercise: " + self.person.RMTestExB)
        self.RMTestExBLabel.pack()

        self.RMTestExBWeightLabel = tk.Label(self)
        self.RMTestExBWeightLabel["text"] = ("1 Rep Max: " + self.person.RMTestExBWeight)
        self.RMTestExBWeightLabel.pack()

   def showRMPredictResult(self, person):
       self.RMPredictResultLabel = tk.Label(self)
       self.RMPredictResultLabel["text"] = "1RM Predicted"

       self.RMPredictExLabel = tk.Label(self)
       self.RMPredictExLabel["text"] = ("Exercise: " + self.person.RMPredictEx)
       self.RMPredictExLabel.pack()

       self.RMPredictWeightLabel = tk.Label(self)
       self.RMPredictWeightLabel["text"] = ("1 Rep Max: " + str(person.getRepMaxPredict()))
       self.RMPredictWeightLabel.pack()

   def showGripStrengthResult(self, person):
       self.GripStrengthLabel = tk.Label(self)
       self.GripStrengthLabel["text"] = "Grip Strength"
       self.GripStrengthLabel.pack()

       self.GripStrengthLeftLabel = tk.Label(self)
       self.GripStrengthLeftLabel["text"] = ("Left Hand(kg): " + self.person.gripStrengthLeft)
       self.GripStrengthLeftLabel.pack()

       self.GripStrengthRightLabel = tk.Label(self)
       self.GripStrengthRightLabel["text"] = ("Right Hand(kg): " + self.person.gripStrengthRight)
       self.GripStrengthRightLabel.pack()

   def showPushUpResult(self, person):
       self.PushUpLabel = tk.Label(self)
       self.PushUpLabel["text"] = "Push Ups"
       self.PushUpLabel.pack()

       self.PushUpNumLabel = tk.Label(self)
       self.PushUpNumLabel["text"] = ("Number: " + self.person.pushUpNum)
       self.PushUpNumLabel.pack()

   def showCurlUpResult(self, person):
       self.CurlUpLabel = tk.Label(self)
       self.CurlUpLabel["text"] = "10cm Curl Ups"
       self.CurlUpLabel.pack()

       self.CurlUpNumLabel = tk.Label(self)
       self.CurlUpNumLabel["text"] = ("Number: " + self.person.curlUpNum)
       self.CurlUpNumLabel.pack()

   def showFrontPlankResult(self, person):
       self.FrontPlankLabel = tk.Label(self)
       self.FrontPlankLabel["text"] = "Front Plank"
       self.FrontPlankLabel.pack()

       self.FrontPlankTime = tk.Label(self)
       self.FrontPlankTime["text"] = ("Time(sec.): " + self.person.plankTime)
       self.FrontPlankTime.pack()

   def showWallSitResult(self, person):
       self.WallSitLabel = tk.Label(self)
       self.WallSitLabel["text"] = "Wall Sit"
       self.WallSitLabel.pack()

       self.WallSitTime = tk.Label(self)
       self.WallSitTime["text"] = ("Time(sec.): " + self.person.wallSitTime)
       self.WallSitTime.pack()

   def showSitReachResult(self, person):
       self.SitReachLabel = tk.Label(self)
       self.SitReachLabel["text"] = "Sit and Reach"
       self.SitReachLabel.pack()

       self.SitReachResult = tk.Label(self)
       self.SitReachResult["text"] = ("Max. Distance(cm): " + self.person.sitReachDist)
       self.SitReachResult.pack()

   def showSLStanceResult(self, person):
       self.SLStanceLabel = tk.Label(self)
       self.SLStanceLabel["text"] = "Single Leg Stance Test"
       self.SLStanceLabel.pack()

       self.SLStanceLeftOpen = tk.Label(self)
       self.SLStanceLeftOpen["text"] = ("Left Leg Eyes Open Time(sec.): " + self.person.SLOpenLeft)
       self.SLStanceLeftOpen.pack()

       self.SLStanceRightOpen = tk.Label(self)
       self.SLStanceRightOpen["text"] = ("Right Leg Eyes Open Time(sec.): " + self.person.SLOpenRight)
       self.SLStanceRightOpen.pack()

       self.SLStanceLeftClosed = tk.Label(self)
       self.SLStanceLeftClosed["text"] = ("Left Leg Eyes Closed Time(sec.): " + self.person.SLCloseLeft)
       self.SLStanceLeftClosed.pack()

       self.SLStanceRightClosed = tk.Label(self)
       self.SLStanceRightClosed["text"] = ("Right Leg Eyes Closed Time(sec.): " + self.person.SLCloseRight)
       self.SLStanceRightClosed.pack()

   def showDeepSquatAssessResult(self, person):
       self.deepSquatAssessLabel = tk.Label(self)
       self.deepSquatAssessLabel["text"] = "Deep Squat Assessment"
       self.deepSquatAssessLabel.pack()

       self.deepSquatRatingLabel = tk.Label(self)
       self.deepSquatRatingLabel["text"] = ("Rating: " + self.person.deepSquatRate)
       self.deepSquatRatingLabel.pack()

   def showWallSlideAssessResult(self, person):
       self.wallSlideLabel = tk.Label(self)
       self.wallSlideLabel["text"] = "Wall Slide Assessment"
       self.wallSlideLabel.pack()

       self.wallSlideRatingLabel = tk.Label(self)
       self.wallSlideRatingLabel["text"] = ("Rating: " + self.person.wallSlideRate)
       self.wallSlideRatingLabel.pack()

   def showHipHingeAssessResult(self, person):
       self.hipHingeLabel = tk.Label(self)
       self.hipHingeLabel["text"] = "Hip Hinge Assessment"
       self.hipHingeLabel.pack()

       self.hipHingeRatingLabel = tk.Label(self)
       self.hipHingeRatingLabel["text"] = ("Rating: " + self.person.hipHingeRate)
       self.hipHingeRatingLabel.pack()

   def showPlankAssessResult(self, person):
       self.plankAssessLabel = tk.Label(self)
       self.plankAssessLabel["text"] = "Front Plank Assessment"
       self.plankAssessLabel.pack()

       self.plankRatingLabel = tk.Label(self)
       self.plankRatingLabel["text"] = ("Rating: " + self.person.frontPlankRate)
       self.plankRatingLabel.pack()

   def loadData(self, person):
        
       self.Results = tk.Label(self)
       self.Results["text"] = "Results"
       self.Results.pack()

       if "VertJump" in person.framesChecked:
        self.showVertJumpResult(person)

       if "BMIframe" in person.framesChecked:
        self.showBMIresult(person)

       if "Circumference" in person.framesChecked: # change self.person.height
        self.showCircumferenceResult(person)

       if "ThreeSiteSkinfold" in person.framesChecked:
        self.showThreeSiteSkinfoldResult(person)

       if "SvnSiteSkinfold" in person.framesChecked:
        self.showSvnSiteSkinfoldResult(person)

       if "ModAst" in person.framesChecked:
        self.showModAstResult(person)

       if "Ebelling" in person.framesChecked:
        self.showEbbelingResult(person)

       if "Rockport" in person.framesChecked:
        self.showRockportResult(person)

       if "Coopers" in person.framesChecked:
        self.showCoopersResult(person)

       if "MBtoss" in person.framesChecked:
        self.showMBTossResult(person)

       if "RMtest" in person.framesChecked:
        self.showRMTestResult(person)

       if "RMpredict" in person.framesChecked:
        self.showRMPredictResult(person)

       if "GripStrength" in person.framesChecked:
        self.showGripStrengthResult(person)

       if "PushUps" in person.framesChecked:
        self.showPushUpResult(person)

       if "CurlUps" in person.framesChecked:
        self.showCurlUpResult(person)

       if "FrontPlank" in person.framesChecked:
        self.showFrontPlankResult(person)

       if "WallSit" in person.framesChecked:
        self.showWallSitResult(person)

       if "SitReach" in person.framesChecked:
        self.showSitReachResult(person)

       if "SLstance" in person.framesChecked:
        self.showSLStanceResult(person)

       if "DeepSquat" in person.framesChecked:
        self.showDeepSquatAssessResult(person)

       if "WallSlide" in person.framesChecked:
        self.showWallSlideAssessResult(person)

       if "HipHinge" in person.framesChecked:
        self.showHipHingeAssessResult(person)

       if "PlankEnd" in person.framesChecked:
        self.showPlankAssessResult(person)

       self.BackButton = BackButton(self, self.controller)
       self.BackButton.pack()

       self.SaveButton = tk.Button(self)
       self.SaveButton['text'] = "Save"
       self.SaveButton['fg'] = "black"
       self.SaveButton['command'] = self.savePerson
       self.SaveButton.pack()

       self.PrintButton = tk.Button(self)
       self.PrintButton['text'] = "Print"
       self.PrintButton['fg'] = "black"
       self.PrintButton['command'] = self.printPerson
       self.PrintButton.pack()

       self.QuitButton = QuitButton(self, self.controller)
       self.QuitButton.pack()

   #def saveData(self, person):
