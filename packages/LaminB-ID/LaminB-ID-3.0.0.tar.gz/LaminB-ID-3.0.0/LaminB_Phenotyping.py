#!/Applications/anaconda3/bin/python

import sys

Explanation = """
The script can be executed at the command line using arguments where the first argument is the file name 
and the second is the separator. The expected format of the file is csv or txt format. 
The first row is expected to be the header. The title of each column is expected to be exactly 
worded as the output from ImageJ including capitalization and spaces. The column names are 
written into the code and it if slightly different then the file will result in errors.
This is a potential area to check if the script does not work properly.
The code is expected to handle common errors gracefully. 
"""


if len(sys.argv) == 1:
    File = input("Please enter the full name of the file to open including the format (.csv or .txt): ")
    Separator = input("Please enter the delimiter of the file (tab key, space key, or ',': ) ")
    while Separator != "\t" and Separator != " " and Separator != ",":
        print("This script only allows the three above delimiters, enter a valid delimiter or change the file format")
        Separator = input("Please enter the delimiter of the file ('tab', space, or ',': ) ")

# File = "LaminBTestMeasures_ExcelBlanks.csv"
# Separator = ","
else:
    if sys.argv[1] == "-help":
        print(Explanation)
        exit()
    else:
        File = sys.argv[1]
        if len(sys.argv) == 2:
            Separator = input("Please enter the delimiter of the file (tab, space, or ',': ) ")
            while Separator != "\t" and Separator != " " and Separator != ",":
                print("This script only allows the three above delimiters, "
                      "enter a valid delimiter or change the file format")
                Separator = input("Please enter the delimiter of the file ('tab', space, or ',': ) ")
        else:
            Separator = sys.argv[2]

try:
    FileRead = open(File, "r")
except FileNotFoundError:
    print()
    print("The file does not exist or cannot be properly opened")
    print("Check that the file name has the correct spelling and has the proper format (.csv or .txt)")
    print("Ensure that the file is available in the current directory (folder)")
    exit()
OutputName = File.split(".")
FileWrite = open(OutputName[0]+"_Phenotypes."+OutputName[1], "w")

Header = FileRead.readline().rstrip("\r").rstrip("\n").split(Separator)

MeasuresList = ["EllipseFlatness", "Moment3", "Moment2", "NumberOfObjects"]

# This is the indexing of the header which can cause problems with incorrect spelling
try:
    EllipseFlatnessIndex = Header.index("Ell_Flatness")
except ValueError:
    print()
    print("The file is in an incorrect format or the separator inputted is incorrect")
    exit()
Moment3Index = Header.index("Moment 3")
Moment2Index = Header.index("Moment 2")
NumberOfObjectsIndex = Header.index("NbObjects")
LabelIndex = Header.index("Label")

EllipseFlatnessList = []
Moment3List = []
Moment2List = []
NumberOfObjectsList = []

BlankLineIndexes = []
Phenotypes = []

Count = 0
for Line in FileRead:
    Line.rstrip("\r").rstrip("\n")
    LineList = Line.split(Separator)
    if LineList[LabelIndex] == "":  # Condition to handle a blank line or one without measurement data
        BlankLineIndexes.append(Count)
        Count += 1
    else:
        EllipseFlatnessList.append(float(LineList[EllipseFlatnessIndex]))
        Moment3List.append(float(LineList[Moment3Index]))
        Moment2List.append(float(LineList[Moment2Index]))
        NumberOfObjectsList.append(float(LineList[NumberOfObjectsIndex]))
        Phenotypes.append("Ring,")
        Count += 1

FileRead.close()

RemovedIndexes = []

InitialAverage = 1
CurrentAverage = 0
while InitialAverage != CurrentAverage:
    InitialAverage = sum(NumberOfObjectsList)/(len(NumberOfObjectsList) - len(RemovedIndexes))
    for Value in NumberOfObjectsList:
        CurrentAverage = sum(NumberOfObjectsList)/(len(NumberOfObjectsList) - len(RemovedIndexes))
        if Value > CurrentAverage*3.3:  # Condition where cell is punctate phenotype
            ToBeRemoved = NumberOfObjectsList.index(Value)
            RemovedIndexes.append(ToBeRemoved)

            NumberOfObjectsList[ToBeRemoved] = 0
            EllipseFlatnessList[ToBeRemoved] = 0
            Moment3List[ToBeRemoved] = 0
            Moment2List[ToBeRemoved] = 0

            Phenotypes[ToBeRemoved] = "Punctate,"
PunctateNbObjectsAve = CurrentAverage

# Make very similar block of code as above for each different phenotype that is to be removed

# Next block of code should remove all Folded or invaginated cells from lists, if 1.4x above Moment 3 average
# Store as Invagination in the Phenotype list

InternalStainingMoment2 = []
InitialAverage = 1
CurrentAverage = 0
while InitialAverage != CurrentAverage:
    InitialAverage = sum(Moment3List)/(len(Moment3List) - len(RemovedIndexes))
    for Value in Moment3List:
        CurrentAverage = sum(Moment3List)/(len(Moment3List) - len(RemovedIndexes))
        if Value > CurrentAverage * 3.05:
            ToBeRemoved = Moment3List.index(Value)
            RemovedIndexes.append(ToBeRemoved)

            InternalStainingMoment2.append(Moment2List[ToBeRemoved])

            EllipseFlatnessList[ToBeRemoved] = 0
            Moment3List[ToBeRemoved] = 0
            # Moment2List[ToBeRemoved] = 0
            Phenotypes[ToBeRemoved] = "Invagination,"
InternalStainingMom2Ave = CurrentAverage

# Create a new loop which loops through Phenotype list, if Phenotype is Invagination,
# store the average of Moment 2 in a new list. Then create another loop similar to loops to define phenotypes.
# Cells are Folded if Moment 2 measurement is 1.3x above the current average

InitialAverage = 1
CurrentAverage = 0
InternalStainingRemovedIndexes = []
NoInternalStaining = False
while InitialAverage != CurrentAverage:
    if len(InternalStainingMoment2) == 0:
    	CurrentAverage = InitialAverage
    	NoInternalStaining = True
    else:
        InitialAverage = sum(InternalStainingMoment2)/(len(InternalStainingMoment2) - len(InternalStainingRemovedIndexes))
        for Value in InternalStainingMoment2:
            CurrentAverage = sum(InternalStainingMoment2)/(len(InternalStainingMoment2)-len(InternalStainingRemovedIndexes))
            if Value > CurrentAverage * 1.4:
                ToBeRemoved = InternalStainingMoment2.index(Value)
                InternalStainingRemovedIndexes.append(ToBeRemoved)
                InternalStainingMoment2[ToBeRemoved] = 0
                FoldedIndex = Moment2List.index(Value)
                Phenotypes[FoldedIndex] = "Folded,"
FoldedMom2Ave = CurrentAverage

# Next loop is to remove the diffuse phenotype when flatness value is 1.4x higher than the current average

InitialAverage = -1
CurrentAverage = 0
while InitialAverage != CurrentAverage:
    InitialAverage = sum(EllipseFlatnessList)/(len(EllipseFlatnessList)-len(RemovedIndexes))
    for Value in EllipseFlatnessList:
        CurrentAverage = sum(EllipseFlatnessList)/(len(EllipseFlatnessList)-len(RemovedIndexes))
        if Value > CurrentAverage*2.1:
            ToBeRemoved = EllipseFlatnessList.index(Value)
            RemovedIndexes.append(ToBeRemoved)
            EllipseFlatnessList[ToBeRemoved] = 0
            Moment3List[ToBeRemoved] = 0
            Phenotypes[ToBeRemoved] = "Diffuse,"
DiffuseEllFlatnessAve = CurrentAverage

# The last loop is to remove the incomplete phenotype from the remaining population.
# Cells are incomplete when Moment3 measurement are 0.8x the current average

InitialAverage = -1
CurrentAverage = 0
while InitialAverage != CurrentAverage:
    InitialAverage = sum(Moment3List)/(len(Moment3List)-len(RemovedIndexes))
    for Value in Moment3List:
        CurrentAverage = sum(Moment3List)/(len(Moment3List)-len(RemovedIndexes))
        if 0 < Value < CurrentAverage * 0.39:
            ToBeRemoved = Moment3List.index(Value)
            RemovedIndexes.append(ToBeRemoved)
            Moment3List[ToBeRemoved] = 0
            Phenotypes[ToBeRemoved] = "Incomplete,"
IncompleteMom3Ave = CurrentAverage

# Also print out total count for each phenotype in addition to adding phenotype to each entry in the output file
# Do this by creating a list containing the different phenotypes and a loop using the .count() method

print("Control group totals:")
DistinctPhenotypes = ["Ring,", "Diffuse,", "Punctate,", "Incomplete,", "Invagination,", "Folded,"]
for Category in DistinctPhenotypes:
    Total = Phenotypes.count(Category)
    print(Category, "count:", Total)
print("The percent of cells with abnormal staining is: ", end="") 
print((Phenotypes.count("Punctate,")+Phenotypes.count("Incomplete,")+Phenotypes.count("Invagination,")+Phenotypes.count("Folded,"))/len(Phenotypes)*100)
if NoInternalStaining:
    print()
    print("Warning!! No cells in the control group were identified with Internal staining")
    print("- (the Invagination or the Folded staining phenotype). ")
    print("This means that cells in the experimental group cannot be classified as Invagination.")
    print("Cells that may have an Invaginated phenotype will be classified as Folded")
    print("The percent of cells with abnormal staining calculation is not affected.")

FileRead = open(File, "r")
FileWrite.write("Phenotype,")
FileWrite.write(FileRead.readline())

PrintCount = 0
PhenotypeCount = 0
for Line in FileRead:
    if PrintCount in BlankLineIndexes:
        FileWrite.write(",")
        FileWrite.write(Line)
        PrintCount += 1
    else:
        FileWrite.write(Phenotypes[PhenotypeCount])
        FileWrite.write(Line)
        PrintCount += 1
        PhenotypeCount += 1

FileRead.close()
FileWrite.close()


# Add code to prompt for second file (siRNA Treatment file), put values of interest in 
# new lists with siA1 suffix. File can be assigned to the initial (same) variable since
# the original file is no longer needed
if len(sys.argv) == 3:
    siA1File = input("Please enter the full name of the siRNA treatment file to open including the format (.csv or .txt): ")
else:
    siA1File = sys.argv[3]

try:
    siA1FileRead = open(siA1File, "r")
except FileNotFoundError:
    print()
    print("The file does not exist or cannot be properly opened")
    print("Check that the file name has the correct spelling and has the proper format (.csv or .txt)")
    print("Ensure that the file is available in the current directory (folder)")
    exit()
siA1OutputName = siA1File.split(".")
siA1FileWrite = open(siA1OutputName[0]+"_Phenotypes."+siA1OutputName[1], "w")

siA1Header = siA1FileRead.readline().rstrip("\r").rstrip("\n").split(Separator)

try:
    EllipseFlatnessIndexsiA1 = siA1Header.index("Ell_Flatness")
except ValueError:
    print()
    print("The file is in an incorrect format or the separator inputted is incorrect")
    exit()
Moment3IndexsiA1 = siA1Header.index("Moment 3")
Moment2IndexsiA1 = siA1Header.index("Moment 2")
NumberOfObjectsIndexsiA1 = siA1Header.index("NbObjects")
LabelIndexsiA1 = siA1Header.index("Label")

EllipseFlatnessListsiA1 = []
Moment3ListsiA1 = []
Moment2ListsiA1 = []
NumberOfObjectsListsiA1 = []

BlankLineIndexessiA1 = []
PhenotypessiA1 = []

Count = 0
for Line in siA1FileRead:
    Line.rstrip("\r").rstrip("\n")
    LineList = Line.split(Separator)
    if LineList[LabelIndexsiA1] == "":  # Condition to handle a blank line or one without measurement data
        BlankLineIndexessiA1.append(Count)
        Count += 1
    else:
        EllipseFlatnessListsiA1.append(float(LineList[EllipseFlatnessIndexsiA1]))
        Moment3ListsiA1.append(float(LineList[Moment3IndexsiA1]))
        Moment2ListsiA1.append(float(LineList[Moment2IndexsiA1]))
        NumberOfObjectsListsiA1.append(float(LineList[NumberOfObjectsIndexsiA1]))
        PhenotypessiA1.append("Ring,")
        Count += 1

siA1FileRead.close()

RemovedIndexessiA1 = []


for Value in NumberOfObjectsListsiA1:
    if Value > PunctateNbObjectsAve*3.3:  # Condition where cell is punctate phenotype
        ToBeRemoved = NumberOfObjectsListsiA1.index(Value)
        RemovedIndexessiA1.append(ToBeRemoved)

        NumberOfObjectsListsiA1[ToBeRemoved] = 0
        EllipseFlatnessListsiA1[ToBeRemoved] = 0
        Moment3ListsiA1[ToBeRemoved] = 0
        Moment2ListsiA1[ToBeRemoved] = 0

        PhenotypessiA1[ToBeRemoved] = "Punctate,"
        
        
InternalStainingMoment2siA1 = []
for Value in Moment3ListsiA1:
    if Value > InternalStainingMom2Ave * 3.05:
        ToBeRemoved = Moment3ListsiA1.index(Value)
        RemovedIndexessiA1.append(ToBeRemoved)

        InternalStainingMoment2siA1.append(Moment2ListsiA1[ToBeRemoved])

        EllipseFlatnessListsiA1[ToBeRemoved] = 0
        Moment3ListsiA1[ToBeRemoved] = 0
        # Moment2List[ToBeRemoved] = 0
        PhenotypessiA1[ToBeRemoved] = "Invagination,"
        
InternalStainingRemovedIndexessiA1 = []        
for Value in InternalStainingMoment2siA1:
        if Value > FoldedMom2Ave * 1.4:
            ToBeRemoved = InternalStainingMoment2siA1.index(Value)
            InternalStainingRemovedIndexessiA1.append(ToBeRemoved)
            InternalStainingMoment2siA1[ToBeRemoved] = 0
            FoldedIndex = Moment2ListsiA1.index(Value)
            PhenotypessiA1[FoldedIndex] = "Folded,"
            
            
for Value in EllipseFlatnessListsiA1:
        if Value > DiffuseEllFlatnessAve*2.1:
            ToBeRemoved = EllipseFlatnessListsiA1.index(Value)
            RemovedIndexessiA1.append(ToBeRemoved)
            EllipseFlatnessListsiA1[ToBeRemoved] = 0
            Moment3ListsiA1[ToBeRemoved] = 0
            PhenotypessiA1[ToBeRemoved] = "Diffuse,"
            
            
for Value in Moment3ListsiA1:
        if 0 < Value < IncompleteMom3Ave * 0.39:
            ToBeRemoved = Moment3ListsiA1.index(Value)
            RemovedIndexessiA1.append(ToBeRemoved)
            Moment3ListsiA1[ToBeRemoved] = 0
            PhenotypessiA1[ToBeRemoved] = "Incomplete,"
            
print()
print("Treatment group totals:")
for Category in DistinctPhenotypes:
    Total = PhenotypessiA1.count(Category)
    print(Category, "count:", Total)
print("The percent of cells with abnormal staining is: ", end="") 
print((PhenotypessiA1.count("Punctate,")+PhenotypessiA1.count("Incomplete,")+PhenotypessiA1.count("Invagination,")+PhenotypessiA1.count("Folded,"))/len(PhenotypessiA1)*100)

siA1FileRead = open(siA1File, "r")
siA1FileWrite.write("Phenotype,")
siA1FileWrite.write(siA1FileRead.readline())

PrintCount = 0
PhenotypeCount = 0
for Line in siA1FileRead:
    if PrintCount in BlankLineIndexessiA1:
        siA1FileWrite.write(",")
        siA1FileWrite.write(Line)
        PrintCount += 1
    else:
        siA1FileWrite.write(PhenotypessiA1[PhenotypeCount])
        siA1FileWrite.write(Line)
        PrintCount += 1
        PhenotypeCount += 1

siA1FileRead.close()
siA1FileWrite.close()
