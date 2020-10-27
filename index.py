import numpy
from chess import \
    random_position, \
    check_tester, \
    random_position2, \
    oracle

mock_position = "*k***x*r******p*B***k**q****************P**b***P****PPP*RK***X*R"


beef = 0

for pos in mock_position:
    if pos == "p":
        print(pos,beef)
    beef = beef+1









    print(mock_position[14])


