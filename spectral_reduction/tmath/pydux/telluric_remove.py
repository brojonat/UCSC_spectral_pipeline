def telluric_remove(bstarwave, bstar, bairmass, wave, object, airmass, variance):
    import numpy as np
    import pdb
    import matplotlib.pyplot as plt
    from tmath.wombat.inputter import inputter
    from tmath.wombat.yesno import yesno
    from tmath.wombat.womscipyrebin import womscipyrebin
    from tmath.wombat.womget_element import womget_element
    from tmath.pydux.xcor import xcor
    from tmath.pydux.finalscaler import finalscaler
    bstartmp=womscipyrebin(bstarwave,bstar,wave)
#    plt.cla()
#    plt.plot(bstarwave,bstartmp)
#    plt.pause(0.01)
#    answer=yesno('y')
    print('\nThe ratio of airmasses (object/B-star) is {}'.format(airmass/bairmass))
    if (airmass/bairmass > 3.0) or (airmass/bairmass < 0.33):
        print('\nWARNING: OBJECT AND B-STAR HAVE WILDLY DIFFERENT')
        print('AIRMASSES: ATMOSPHERIC BAND DIVISION MAY BE LOUSY\n')

    wmin=wave[0]
    wmax=wave[-1]
    npix=len(object)
    wdelt=wave[1]-wave[0]
    print('wdelt',wdelt)
    lag=np.zeros(3)
    lagflag=[False]*3
    xfactor=10
    maxlag=200
    print('\nCross-correlating object with B-star spectrum\n')
    if (wmin < 6200) and (wmax > 6400) and (wmax < 6900):
        indblue=womget_element(wave,6200)
        indred=womget_element(wave,6400)
        lag[0]=xcor(object[indblue:indred+1],bstartmp[indblue:indred+1],xfactor,maxlag)
        lagflag[0]=True
        print('The shift at the 6250A band is {} angstroms'.format(lag[0]*wdelt))
    if (wmin < 6800) and (wmax > 6500):
        indblue=womget_element(wave,6800)
        indred=womget_element(wave,6950)
        obb=object[indblue:indred+1]
        bb=bstartmp[indblue:indred+1]
        lag[1]=xcor(obb,bb,xfactor,maxlag)
        lagflag[1]=True
        print('The shift at the B band is {} angstroms'.format(lag[1]*wdelt))
    if (wmin < 7500) and (wmax > 8000):
        indblue=womget_element(wave,7500)
        indred=womget_element(wave,8000)
        lag[2]=xcor(object[indblue:indred+1],bstartmp[indblue:indred+1],xfactor,maxlag)
        print('The shift at the A band is {} angstroms'.format(lag[2]*wdelt))
        lagflag[2]=True
    if (sum(lagflag) > 0):
        avglag=np.sum(lag)/sum(lagflag)
        angshift=avglag*wdelt
        print('The mean shift is {} Angstroms'.format(angshift))
    else:
        angshift=0.0
    bstartmpcopy=bstartmp.copy()
    telluric_done = False
    plt.clf()
    while (not telluric_done):
        bstartmp=bstartmpcopy.copy()
        tmp=womscipyrebin(wave+angshift,bstartmp,wave)
        bstartmp=tmp.copy()
        bstartmp=bstartmp**((airmass/bairmass)**0.55)
        newobject=object/bstartmp
        bvar=variance/bstartmp
        print('\nPlotting before and after atmospheric band correction\n')
        plt.cla()
        ymin,ymax=finalscaler(object)
        plt.plot(wave,object,drawstyle='steps-mid',color='r')
        plt.plot(wave,newobject,drawstyle='steps-mid',color='k')
        plt.pause(0.01)
        print('Is this OK?')
        answer=yesno('y')
        if (answer == 'n'):
            angshift=inputter('Enter B-star shift in Angstroms: ','float',False)
        else:
            telluric_done = True
    return newobject, bvar, angshift
            
