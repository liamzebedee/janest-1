package test

func main() {

	var out [64]byte
	// out[0..55] = x[0..55] + 128 * x[56..111] + -256 * x[112..167] + 128 * x[168..223]
	// which is another way of saying
	// out[0..55] = 

    for i in range(0, 56):
        s = x[0 + i] + 128.0 * x[i + 56] + -256.0 * x[i + 112] + 128.0 * x[i + 168]
        out[0 + i] = s if s > 0 else 0.0 # ReLu


    var x [64]byte
    var out [8]byte
	
	// set the bits 56..63 to the bits 224..231
	// do this using a mask and no for loop
	
	// buf[56..64] = x[224..231]
    copy(buf[:], x[224:232])
	mask := byte(0xFF) << 56
	buf[0] = buf[0] & mask
	copy(x[56:64], buf[:])

    for i in range(0, 8):
        s = x[224 + i]
		// buf[56..64] = x[224..231]
        out[56 + i] = s if s > 0 else 0.0 # ReLu

}