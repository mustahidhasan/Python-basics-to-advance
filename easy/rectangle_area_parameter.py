# given two integer height and width of a rectangle find
# area = height x width
# parameter = 2 * (heihgt + weight)
l, w = map(int, input().split())
print(f"{l*w} {2*(l+w)}")