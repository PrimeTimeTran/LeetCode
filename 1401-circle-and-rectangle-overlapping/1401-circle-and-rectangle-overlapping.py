class Solution:
  def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
    # Find the closest horizontal distance to the rectangle
    closestXDistance = self.calculateDistanceToRange(x1, x2, xCenter)

    # Find the closest vertical distance to the rectangle
    closestYDistance = self.calculateDistanceToRange(y1, y2, yCenter)

    # If distance to the closest point <= radius, they overlap
    return (
      closestXDistance * closestXDistance + closestYDistance * closestYDistance
      <= radius * radius
    )

  def calculateDistanceToRange(self, rangeStart, rangeEnd, point):
    # Point is already inside the range
    if rangeStart <= point <= rangeEnd:
      return 0

    # Otherwise, return distance to the nearest boundary
    return rangeStart - point if point < rangeStart else point - rangeEnd
