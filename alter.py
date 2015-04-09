from pippi import dsp

snd = dsp.read('get.wav').data

numgrains = 40 
lens = [ 1 for _ in range(numgrains/2) ]
lens = lens + dsp.wavetable('hann', numgrains)[len(lens):]
lens = [ dsp.mstf(l * 40 + 30) for l in lens ]

out = ''

numsegs = 8
spos = 0

for s in range(numsegs):
    lpos = spos
    rpos = spos + dsp.mstf(100)
    for i in range(numgrains):
        l = dsp.cut(snd, lpos, lens[i])
        r = dsp.cut(snd, rpos, lens[i])

        lpos += dsp.mstf(dsp.rand(1, 10))
        rpos += dsp.mstf(dsp.rand(1, 10))

        out += dsp.pan(l, 0)
        out += dsp.pan(r, 1)

    spos += dsp.flen(snd) / 8

dsp.write(out, 'alter')
