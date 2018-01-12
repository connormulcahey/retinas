# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

# Step 1 - read input into data sctructure

class Vessel:

	def __init__(self, vesselType, vesselWidth):
		self.vesselType = vesselType
		self.vesselWidth = vesselWidth

filename = sys.argv[1]

print("reading " + filename + "...")

lineNumber = 0

vessels = []

for line in open(filename, 'r'):

    if lineNumber < 4:
    	# first 4 lines (indexes 0, 1, 2, 3) are header info
    	lineNumber += 1
    	continue

    lineSplitIntoKVPairs = line.split('  ')
    vesselTypeString = lineSplitIntoKVPairs[7].split(':')[1][:1]
    vesselWidth = lineSplitIntoKVPairs[8].split(':')[1]

    print "Line " + str(lineNumber + 1) + " type: " + vesselTypeString
    print "Line " + str(lineNumber + 1) + " width: " + vesselWidth
    print "\n"

    newVessel = Vessel(vesselType=vesselTypeString, vesselWidth=float(vesselWidth))
    vessels.append(newVessel)

    lineNumber += 1

print str(len(vessels)) + " vessels read"
print "\n"

 # Step 2 - calculations

# Get the average of the 6 largest veins.
# Get the average of the 6 largest arteries.
# Divide the average of the veins, by the arteries.

# If there are more than 6 veins and/or arteries, exclude the smallest ones from the set.
# If there is less than 6 veins/arteries (say only 5 veins and 7 arteries), then get the average of the lesser vessels for both (so average of 5 veins and 5 arteries)

# Ideally, if possible, in the above instance, also get the average if you include 6 arteries

i = 1

arteryWidths = []
veinWidths = []

for v in vessels:

	if (v.vesselType == "V"):
		veinWidths.append(v.vesselWidth)
	else:
		arteryWidths.append(v.vesselWidth)

sortedArteryWidths = list(reversed(sorted(arteryWidths)))
sortedVeinWidths = list(reversed(sorted(veinWidths)))

print "sortedArteryWidths: " + str(sortedArteryWidths)
print "sortedVeinWidths: " + str(sortedVeinWidths)
print "\n"

minSampleSize = min(len(sortedVeinWidths), len(sortedArteryWidths))

if minSampleSize < 6:
	print "Min sample size is " + str(minSampleSize)
	splicedVeinSample = sortedVeinWidths[:minSampleSize]
	splicedArterySample = sortedArteryWidths[:minSampleSize]
	minSampleAverageOfVeins = reduce(lambda x, y: x + y, splicedVeinSample) / minSampleSize
	minSampleAverageOfArteries = reduce(lambda x, y: x + y, splicedArterySample) / minSampleSize
	print "Average of " + str(minSampleSize) + " (min sample size) largest veins:" + str(minSampleAverageOfVeins)
	print "Average of " + str(minSampleSize) + " (min sample size) largest arteries:" + str(minSampleAverageOfArteries)

print "\n"

if len(sortedVeinWidths) > 5:
	splicedVeinSample = sortedVeinWidths[:6]
	averageOfSixLargestVeins = reduce(lambda x, y: x + y, splicedVeinSample) / 6
	print "Average of 6 largest arteries: " + str(averageOfSixLargestVeins)

if len(sortedArteryWidths) > 5:
	splicedArterySample = sortedArteryWidths[:6]
	averageOfSixLargestArteries = reduce(lambda x, y: x + y, splicedArterySample) / 6
	print "Average of 6 largest arteries: " + str(averageOfSixLargestArteries)

print "================="
print "DONE!"
print "================="

