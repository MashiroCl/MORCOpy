from .metricCalculation import *

class Qmood():
    def __init__(self):
        self.DSC=0
        self.NOH=0
        self.ANA=0
        self.DAM=0
        self.DCC=0
        self.CAM=0
        self.MOA=0
        self.MFA=0
        self.NOP=0
        self.CIS=0
        self.NOM=0
        self.Resusability = 0
        self.Flexibility = 0
        self.Understandability = 0
        self.Functionality = 0
        self.Extendibility = 0
        self.Effectiveness = 0

    def calculateSingleQmood(self,jClass,jClassList):
        self.DSC=DSC(jClassList)
        self.NOH=NOH(jClass)
        self.ANA=ANA(jClassList)
        self.DAM=DAM(jClass)
        self.DCC=DCC(jClassList)
        self.CAM=CAM(jClass)
        self.MOA=MOA(jClassList,jClass)
        self.MFA=MFA(jClass)
        self.NOP=NOP(jClass)
        self.CIS=CIS(jClass)
        self.NOM=NOM(jClass)

        self.Resusability = -0.25*self.DCC+0.25*self.CAM+0.5*self.CIS+0.5*self.DSC
        self.Flexibility = 0.25*self.DAM-0.25*self.DCC+0.5*self.MOA+0.5*self.NOP
        self.Understandability = -0.33*self.ANA+0.33*self.DAM-0.33*self.DCC+0.33*self.CAM-0.33*self.NOP-0.33*self.NOM-0.33*self.DSC
        self.Functionality = 0.12*self.CAM+0.22*self.NOP+0.22*self.CIS+0.22*self.DSC+0.22*self.NOH
        self.Extendibility = 0.5*self.ANA-0.5*self.DCC+0.5*self.MFA+0.5*self.NOP
        self.Effectiveness = 0.2*self.ANA+0.2*self.DAM+0.2*self.MOA+0.2*self.MFA+0.2*self.NOP

    def calculateQmood(self,jClassList):
        'obtain metrics for all classes and calculate the average value '
        sDSC, sNOH, sANA, sDAM, sDCC, sCAM, sMOA, sMFA, sNOP, sCIS, sNOM = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        NOP_not0_count = 0
        NOM_not0_count = 0
        for each in jClassList:
            sDSC+=DSC(jClassList)
            sNOH+=NOH(jClassList)
            sANA+=ANA(jClassList)
            sDAM+=DAM(each)
            sDCC+=DCC(each,jClassList)
            sCAM+=CAM(each)
            sMOA+=MOA(each,jClassList)
            sMFA+=MFA(each)
            # sNOP+=NOP(each)
            curNOP = NOP(each)
            if curNOP!=0:
                sNOP+=curNOP
                NOP_not0_count+=1
            sCIS+=CIS(each)
            # sNOM=NOM(each)
            curNOM = NOM(each)
            if curNOM!=0:
                sNOM+=curNOM
                NOM_not0_count+=1
        lenJCL=len(jClassList)
        self.DSC=sDSC/lenJCL
        self.NOH=sNOH/lenJCL
        self.ANA=sANA/lenJCL
        self.DAM=sDAM/lenJCL
        self.DCC=sDCC/lenJCL
        self.CAM=sCAM/lenJCL
        self.MOA=sMOA/lenJCL
        self.MFA=sMFA/lenJCL
        if NOP_not0_count==0:
            NOP_not0_count=1
        self.NOP=sNOP/NOP_not0_count
        self.CIS=sCIS/lenJCL
        if NOM_not0_count==0:
            NOM_not0_count=1
        self.NOM=sNOM/NOM_not0_count

        print("DSC:{},NOH:{},ANA:{},DAM:{},DCC:{},CAM:{},MOA:{},MFA:{},NOP:{},CIS:{},NOM:{}".format(self.DSC,self.NOH,self.ANA,self.DAM,self.DCC,self.CAM,self.MOA,self.MFA,self.NOP,self.CIS,self.NOM))

        self.Resusability = -0.25*self.DCC+0.25*self.CAM+0.5*self.CIS+0.5*self.DSC
        self.Flexibility = 0.25*self.DAM-0.25*self.DCC+0.5*self.MOA+0.5*self.NOP
        self.Understandability = -0.33*self.ANA+0.33*self.DAM-0.33*self.DCC+0.33*self.CAM-0.33*self.NOP-0.33*self.NOM-0.33*self.DSC
        self.Functionality = 0.12*self.CAM+0.22*self.NOP+0.22*self.CIS+0.22*self.DSC+0.22*self.NOH
        self.Extendibility = 0.5*self.ANA-0.5*self.DCC+0.5*self.MFA+0.5*self.NOP
        self.Effectiveness = 0.2*self.ANA+0.2*self.DAM+0.2*self.MOA+0.2*self.MFA+0.2*self.NOP

        result=dict()
        result["Resusability"]=self.Resusability
        result["Flexibility"] = self.Flexibility
        result["Understandability"] = self.Understandability
        result["Functionality"] = self.Functionality
        result["Extendibility"] = self.Extendibility
        result["Effectiveness"] = self.Effectiveness
        return result

    def getResusability(self):
        return self.Resusability
    def getFlexibility(self):
        return self.Flexibility
    def getUnderstandability(self):
        return self.Understandability
    def getFunctionality(self):
        return self.Functionality
    def getExtendibility(self):
        return self.Extendibility
    def getEffectiveness(self):
        return self.Effectiveness


if __name__=="__main__":
    print("test Qmood calculation")
    qmood=Qmood()
    qmood.calculateQmood()