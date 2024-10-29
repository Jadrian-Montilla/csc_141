import shirts_16
shirts_16.make_shirt("small", "i look big in this")

from shirts_16 import make_shirt
make_shirt("medium", "i dug this out of my shoebox")

from shirts_16 import make_shirt as shirter
shirter("large", "i wear this with my bed")

import shirts_16 as S16
S16.make_shirt("extra small", "designed to fit my finger")

from shirts_16 import *
make_shirt("medium", "i don't tie my shoes, i tape the laces together")