#IB:Input55,Output224(17layerswithinblock)
ib_dims=[55,224,232,64,208,200,212,204,216,208,220,212,224,216,228,220,232,224]

#A:Input224,Output256(18layerswithinblock)
a_dims=[224,336,296,340,332,375,399,410,402,412,404,412,404,408,400,352,288,288,256]

#B:Input256,Output256(13layerswithinblock)
b_dims=[256,319,288,318,288,316,288,312,288,304,288,256,288,256]

#C:Input256,Output256(11layerswithinblock)
c_dims=[256,319,288,318,288,316,288,312,288,304,288,256]

#A':Input256,Output256(18layerswithinblock)
a_prime_dims=[256,368,328,340,332,375,399,410,402,412,404,412,404,408,400,352,288,288,256]

#A'':Input256,Output256(18layerswithinblock)
a_prime_prime_dims=[256,336,328,340,332,375,399,410,402,412,404,412,404,408,400,352,288,288,256]

#FB:Input256,Output48(58layerswithinblock)-Sequenceneedscarefulextraction
#Examplestart/endbasedonanalysis-actuallistwouldbe~59elementslong
fb_dims=[256,256,256,256,256,287,319,318,318,316,316,312,312,304,304,256,192,192,160,223,192,222,192,220,192,216,192,208,192,160,160,192,160,223,192,222,192,220,192,216,192,208,192,160,160,320,320,382,446,444,444,440,440,432,432,416,416,320,192,48]

sequence = open('seq.txt', 'r').read().split(',')

# consume seq until we are wrong