def womfilters(hop):
    """calculate photometric values from spectra"""
    import numpy as np
    import logging
    from tmath.wombat.filtermag import filtermag
    from tmath.wombat.yesno import yesno
    from tmath.wombat.inputter import inputter
    from tmath.wombat.inputter_single import inputter_single
    print('NOTE:  The routine expects an f_lambda spectrum')
    print('       I will try to guess if the spectrum')
    print('       has been scaled by 1E15')
    print(' ')
    print('       Check this before believing fluxes')
    print(' ')
    flux=hop[0].flux.copy()
    if (np.mean(flux) > 0.00001):
        flux = flux *1.e-15

    filtwave=np.zeros((141,10))
    filttran=np.zeros((141,10))
    filtwave[0:21, 1] = [3600.00, 3700.00, 3800.00, 3900.00, \
                         4000.00, 4100.00, 4200.00, 4300.00, \
                         4400.00, 4500.00, 4600.00, 4700.00, \
                         4800.00, 4900.00, 5000.00, 5100.00, \
                         5200.00, 5300.00, 5400.00, 5500.00, \
                         5600.00] 
    filttran[0:21, 1] = [0.00000, 0.03000, 0.13400, 0.56700, \
                         0.92000, 0.97800, 1.00000, 0.97800, \
                         0.93500, 0.85300, 0.74000, 0.64000, \
                         0.53600, 0.42400, 0.32500, 0.23500, \
                         0.15000, 0.09500, 0.04300, 0.00900, \
                         0.00000]
    filtwave[0:24, 2] = [4700.00, 4800.00, 4900.00, 5000.00, \
                      5100.00, 5200.00, 5300.00, 5400.00, \
                      5500.00, 5600.00, 5700.00, 5800.00, \
                      5900.00, 6000.00, 6100.00, 6200.00, \
                      6300.00, 6400.00, 6500.00, 6600.00, \
                      6700.00, 6800.00, 6900.00, 7000.00] 
    filttran[0:24:, 2] = [0.00000, 0.03000, 0.16300, 0.45800, \
                      0.78000, 0.96700, 1.00000, 0.97300, \
                      0.89800, 0.79200, 0.68400, 0.57400, \
                      0.46100, 0.35900, 0.27000, 0.19700, \
                      0.13500, 0.08100, 0.04500, 0.02500, \
                      0.01700, 0.01300, 0.00900, 0.00000]
    filtwave[0:24, 3] = [5500.00, 5600.00, 5700.00, 5800.00, \
                      5900.00, 6000.00, 6100.00, 6200.00, \
                      6300.00, 6400.00, 6500.00, 6600.00, \
                      6700.00, 6800.00, 6900.00, 7000.00, \
                      7100.00, 7200.00, 7300.00, 7400.00, \
                      7500.00, 8000.00, 8500.00, 9000.00]
    filttran[0:24:, 3] = [0.00000, 0.23000, 0.74000, 0.91000, \
                      0.98000, 1.00000, 0.98000, 0.96000, \
                      0.93000, 0.90000, 0.86000, 0.81000, \
                      0.78000, 0.72000, 0.67000, 0.61000, \
                      0.56000, 0.51000, 0.46000, 0.40000, \
                      0.35000, 0.14000, 0.03000, 0.00000]
    filtwave[0:23, 4] = [7000.00, 7100.00, 7200.00, 7300.00, \
                         7400.00, 7500.00, 7600.00, 7700.00, \
                         7800.00, 7900.00, 8000.00, 8100.00, \
                         8200.00, 8300.00, 8400.00, 8500.00, \
                         8600.00, 8700.00, 8800.00, 8900.00, \
                         9000.00, 9100.00, 9200.00]
    filttran[0:23, 4] = [0.00000, 0.02400, 0.23200, 0.55500, \
                         0.78500, 0.91000, 0.96500, 0.98500, \
                         0.99000, 0.99500, 1.00000, 1.00000, \
                         0.99000, 0.98000, 0.95000, 0.91000, \
                         0.86000, 0.75000, 0.56000, 0.33000, \
                         0.15000, 0.03000, 0.00000]

    filtwave[0:24, 0] = [3050.00, 3100.00, 3150.00, 3200.00, \
                      3250.00, 3300.00, 3350.00, 3400.00, \
                      3450.00, 3500.00, 3550.00, 3600.00, \
                      3650.00, 3700.00, 3750.00, 3800.00, \
                      3850.00, 3900.00, 3950.00, 4000.00, \
                      4050.00, 4100.00, 4150.00, 4200.00]
    filttran[0:24, 0] = [0.00000, 0.02000, 0.07700, 0.13500, \
                      0.20400, 0.28200, 0.38500, 0.49300, \
                      0.60000, 0.70500, 0.82000, 0.90000, \
                      0.95900, 0.99300, 1.00000, 0.97500, \
                      0.85000, 0.64500, 0.40000, 0.22300, \
                      0.12500, 0.05700, 0.00500, 0.00000]
    
    filtwave[0:47,5]=[2980., 3005., 3030., 3055., 3080., 3105., 3130.,  \
                      3155., 3180.,3205., 3230., 3255., 3280., 3305., \
                      3330., 3355., 3380., 3405., 3430., 3455., 3480., \
                      3505., 3530., 3555., 3580., 3605., 3630., 3655., \
                      3680., 3705., 3730., 3755., 3780., 3805., 3830., \
                      3855., 3880., 3905., 3930., 3955., 3980., 4005., \
                      4030., 4055., 4080., 4105., 4130.]
    filttran[0:47,5]=[0.    , 0.0014, 0.0071, 0.0127, 0.0198, 0.0314, \
                      0.0464, 0.0629, 0.0794, 0.0949, 0.1093, 0.1229, \
                      0.1352, 0.1458, 0.1545, 0.1617, 0.1679, 0.1737, \
                      0.1786, 0.1819, 0.1842, 0.186 , 0.187 , 0.1868, \
                      0.1862, 0.1858, 0.1853, 0.1841, 0.1812, 0.1754, \
                      0.1669, 0.1558, 0.1419, 0.1247, 0.1054, 0.0851, \
                      0.0634, 0.0405, 0.0216, 0.011 , 0.0062, 0.0032, \
                      0.0015, 0.0008, 0.0006, 0.0003, 0.    ]
    filtwave[0:89,6]=[3630., 3655., 3680., 3705., 3730., 3755., 3780., \
                      3805., 3830., 3855., 3880., 3905., 3930., 3955., \
                      3980., 4005., 4030., 4055., 4080., 4105., 4130., \
                      4155., 4180., 4205., 4230., 4255., 4280., 4305., \
                      4330., 4355., 4380., 4405., 4430., 4455., 4480., \
                      4505., 4530., 4555., 4580., 4605., 4630., 4655., \
                      4680., 4705., 4730., 4755., 4780., 4805., 4830., \
                      4855., 4880., 4905., 4930., 4955., 4980., 5005., \
                      5030., 5055., 5080., 5105., 5130., 5155., 5180., \
                      5205., 5230., 5255., 5280., 5305., 5330., 5355., \
                      5380., 5405., 5430., 5455., 5480., 5505., 5530., \
                      5555., 5580., 5605., 5630., 5655., 5680., 5705., \
                      5730., 5755., 5780., 5805., 5830.]
    filttran[0:89,6]=[0.000e+00, 5.000e-04, 1.300e-03, 2.200e-03, \
                      3.000e-03, 3.900e-03, 5.500e-03, 8.700e-03, \
                      1.620e-02, 3.010e-02, 5.000e-02, 7.450e-02, \
                      1.024e-01, 1.324e-01, 1.629e-01, 1.924e-01, \
                      2.191e-01, 2.419e-01,2.609e-01, 2.767e-01, \
                      2.899e-01, 3.010e-01, 3.105e-01, 3.186e-01, \
                      3.258e-01, 3.324e-01, 3.385e-01, 3.442e-01, \
                      3.496e-01, 3.548e-01, 3.596e-01, 3.640e-01, \
                      3.678e-01, 3.709e-01, 3.736e-01, 3.763e-01, \
                      3.792e-01, 3.827e-01, 3.863e-01, 3.899e-01, \
                      3.931e-01, 3.955e-01, 3.973e-01, 3.986e-01, \
                      3.997e-01, 4.008e-01, 4.019e-01, 4.030e-01, \
                      4.043e-01, 4.057e-01, 4.073e-01, 4.091e-01, \
                      4.110e-01, 4.129e-01, 4.147e-01, 4.165e-01, \
                      4.181e-01, 4.194e-01, 4.201e-01, 4.201e-01, \
                      4.191e-01, 4.169e-01, 4.147e-01, 4.115e-01, \
                      3.988e-01, 3.684e-01, 3.233e-01, 2.690e-01, \
                      2.112e-01, 1.550e-01, 1.043e-01, 6.270e-02, \
                      3.370e-02, 1.900e-02, 1.280e-02, 8.700e-03, \
                      5.700e-03, 3.700e-03, 2.400e-03, 1.700e-03, \
                      1.400e-03, 1.200e-03, 1.000e-03, 9.000e-04, \
                      7.000e-04, 5.000e-04, 3.000e-04, 1.000e-04, 0.000e+00]
    filtwave[0:75,7]=[5380., 5405., 5430., 5455., 5480., 5505., 5530., \
                      5555., 5580., 5605., 5630., 5655., 5680., 5705., \
                      5730., 5755., 5780., 5805., 5830., 5855., 5880., \
                      5905., 5930., 5955., 5980., 6005., 6030., 6055., \
                      6080., 6105., 6130., 6155., 6180., 6205., 6230., \
                      6255., 6280., 6305., 6330., 6355., 6380., 6405., \
                      6430., 6455., 6480., 6505., 6530., 6555., 6580., \
                      6605., 6630., 6655., 6680., 6705., 6730., 6755., \
                      6780., 6805., 6830., 6855., 6880., 6905., 6930., \
                      6955., 6980., 7005., 7030., 7055., 7080., 7105., \
                      7130., 7155., 7180., 7205., 7230.]
    filttran[0:75,7]=[0.000e+00, 1.600e-03, 1.130e-02, 2.970e-02, \
                      5.680e-02, 9.230e-02, 1.356e-01, 1.856e-01, \
                      2.390e-01, 2.917e-01, 3.395e-01, 3.794e-01, \
                      4.116e-01, 4.371e-01, 4.570e-01, 4.723e-01, \
                      4.839e-01, 4.925e-01, 4.990e-01, 5.040e-01, \
                      5.080e-01, 5.112e-01, 5.141e-01, 5.169e-01, \
                      5.194e-01, 5.213e-01, 5.222e-01, 5.220e-01, \
                      5.212e-01, 5.202e-01, 5.197e-01, 5.202e-01, \
                      5.215e-01, 5.233e-01, 5.254e-01, 5.275e-01, \
                      5.294e-01, 5.310e-01, 5.319e-01, 5.320e-01, \
                      5.316e-01, 5.310e-01, 5.305e-01, 5.302e-01, \
                      5.299e-01, 5.290e-01, 5.271e-01, 5.241e-01, \
                      5.211e-01, 5.176e-01, 5.057e-01, 4.775e-01, \
                      4.341e-01, 3.792e-01, 3.162e-01, 2.488e-01, \
                      1.824e-01, 1.225e-01, 7.470e-02, 4.300e-02, \
                      2.470e-02, 1.550e-02, 1.120e-02, 8.300e-03, \
                      5.900e-03, 4.100e-03, 2.900e-03, 2.100e-03, \
                      1.600e-03, 1.300e-03, 1.000e-03, 8.000e-04, \
                      5.000e-04, 2.000e-04, 0.000e+00]
    filtwave[0:89,8]=[6430., 6455., 6480., 6505., 6530., 6555., 6580., \
                      6605., 6630., 6655., 6680., 6705., 6730., 6755., \
                      6780., 6805., 6830., 6855., 6880., 6905., 6930., \
                      6955., 6980., 7005., 7030., 7055., 7080., 7105., \
                      7130., 7155., 7180., 7205., 7230., 7255., 7280., \
                      7305., 7330., 7355., 7380., 7405., 7430., 7455., \
                      7480., 7505., 7530., 7555., 7580., 7605., 7630., \
                      7655., 7680., 7705., 7730., 7755., 7780., 7805., \
                      7830., 7855., 7880., 7905., 7930., 7955., 7980., \
                      8005., 8030., 8055., 8080., 8105., 8130., 8155., \
                      8180., 8205., 8230., 8255., 8280., 8305., 8330., \
                      8355., 8380., 8405., 8430., 8455., 8480., 8505., \
                      8530., 8555., 8580., 8605., 8630.]
    filttran[0:89,8]=[0.000e+00, 1.000e-04, 3.000e-04, 4.000e-04, 5.000e-04, \
                      4.000e-04, 3.000e-04, 5.000e-04, 1.000e-03, 2.100e-03, \
                      3.600e-03, 6.000e-03, 1.110e-02, 2.080e-02, 3.660e-02, \
                      5.970e-02, 9.130e-02, 1.317e-01, 1.779e-01, 2.260e-01, \
                      2.719e-01, 3.125e-01, 3.470e-01, 3.755e-01, 3.978e-01, \
                      4.142e-01, 4.256e-01, 4.331e-01, 4.377e-01, 4.405e-01, \
                      4.416e-01, 4.411e-01, 4.392e-01, 4.358e-01, 4.315e-01, \
                      4.265e-01, 4.214e-01, 4.165e-01, 4.119e-01, 4.077e-01, \
                      4.039e-01, 4.006e-01, 3.975e-01, 3.943e-01, 3.906e-01, \
                      3.862e-01, 3.812e-01, 3.757e-01, 3.700e-01, 3.641e-01, \
                      3.583e-01, 3.526e-01, 3.473e-01, 3.424e-01, 3.379e-01, \
                      3.337e-01, 3.297e-01, 3.259e-01, 3.224e-01, 3.194e-01, \
                      3.169e-01, 3.150e-01, 3.132e-01, 3.111e-01, 3.081e-01, \
                      3.039e-01, 2.996e-01, 2.945e-01, 2.803e-01, 2.493e-01, \
                      2.060e-01, 1.578e-01, 1.118e-01, 7.430e-02, 4.580e-02, \
                      2.570e-02, 1.340e-02, 7.700e-03, 5.500e-03, 3.700e-03, \
                      2.300e-03, 1.500e-03, 1.100e-03, 1.100e-03, 1.100e-03, \
                      9.000e-04, 6.000e-04, 3.000e-04, 0.000e+00]
    filtwave[0:141,9]=[ 7730.,  7755.,  7780.,  7805.,  7830.,  7855.,  7880., \
                       7905., 7930.,  7955.,  7980.,  8005.,  8030.,  8055., \
                       8080.,  8105., 8130.,  8155.,  8180.,  8205.,  8230., \
                       8255.,  8280.,  8305., 8330.,  8355.,  8380.,  8405., \
                       8430.,  8455.,  8480.,  8505., 8530.,  8555.,  8580., \
                       8605.,  8630.,  8655.,  8680.,  8705., 8730.,  8755., \
                       8780.,  8805.,  8830.,  8855.,  8880.,  8905., 8930., \
                       8955.,  8980.,  9005.,  9030.,  9055.,  9080.,  9105.,\
                       9130.,  9155.,  9180.,  9205.,  9230.,  9255.,  9280.,\
                       9305., 9330.,  9355.,  9380.,  9405.,  9430.,  9455., \
                       9480.,  9505., 9530.,  9555.,  9580.,  9605.,  9630., \
                       9655.,  9680.,  9705., 9730.,  9755.,  9780.,  9805.,  \
                       9830.,  9855.,  9880.,  9905., 9930.,  9955.,  9980., \
                       10005., 10030., 10055., 10080., 10105., 10130., 10155.,\
                       10180., 10205., 10230., 10255., 10280., 10305., 10330.,\
                       10355., 10380., 10405., 10430., 10455., 10480., 10505.,\
                       10530., 10555., 10580., 10605., 10630., 10655., 10680.,\
                       10705., 10730., 10755., 10780., 10805., 10830., 10855.,\
                       10880., 10905., 10930., 10955., 10980., 11005., 11030.,\
                       11055., 11080., 11105., 11130., 11155., 11180., 11205.,\
                       11230.]
    filttran[0:141,9]=[0.00e+00, 0.00e+00, 1.00e-04, 1.00e-04, 1.00e-04, \
                       2.00e-04, 2.00e-04, 3.00e-04, 5.00e-04, 7.00e-04, \
                       1.10e-03, 1.70e-03, 2.70e-03, 4.00e-03, 5.80e-03, \
                       8.20e-03, 1.14e-02, 1.55e-02, 2.02e-02, 2.55e-02, \
                       3.11e-02, 3.69e-02, 4.28e-02, 4.84e-02, 5.36e-02, \
                       5.83e-02, 6.25e-02, 6.61e-02, 6.93e-02, 7.20e-02, \
                       7.44e-02, 7.63e-02, 7.79e-02, 7.92e-02, 8.01e-02, \
                       8.08e-02, 8.12e-02, 8.13e-02, 8.12e-02, 8.07e-02, \
                       8.01e-02, 7.91e-02, 7.79e-02, 7.66e-02, 7.50e-02, \
                       7.34e-02, 7.16e-02, 6.98e-02, 6.79e-02, 6.61e-02, \
                       6.42e-02, 6.24e-02, 6.07e-02, 5.90e-02, 5.74e-02, \
                       5.59e-02, 5.46e-02, 5.35e-02, 5.24e-02, 5.15e-02, \
                       5.05e-02, 4.96e-02, 4.85e-02, 4.74e-02, 4.62e-02, \
                       4.50e-02, 4.38e-02, 4.26e-02, 4.15e-02, 4.04e-02, \
                       3.93e-02, 3.83e-02, 3.73e-02, 3.63e-02, 3.53e-02, \
                       3.42e-02, 3.31e-02, 3.19e-02, 3.07e-02, 2.94e-02, \
                       2.80e-02, 2.67e-02, 2.53e-02, 2.40e-02, 2.27e-02, \
                       2.13e-02, 2.01e-02, 1.88e-02, 1.76e-02, 1.65e-02, \
                       1.53e-02, 1.43e-02, 1.32e-02, 1.22e-02, 1.12e-02, \
                       1.03e-02, 9.40e-03, 8.60e-03, 7.80e-03, 7.10e-03, \
                       6.40e-03, 5.80e-03, 5.20e-03, 4.70e-03, 4.20e-03, \
                       3.80e-03, 3.50e-03, 3.10e-03, 2.80e-03, 2.60e-03, \
                       2.40e-03, 2.20e-03, 2.00e-03, 1.90e-03, 1.80e-03, \
                       1.60e-03, 1.50e-03, 1.40e-03, 1.30e-03, 1.20e-03, \
                       1.10e-03, 1.00e-03, 9.00e-04, 8.00e-04, 8.00e-04, \
                       7.00e-04, 7.00e-04, 6.00e-04, 6.00e-04, 5.00e-04, \
                       5.00e-04, 4.00e-04, 4.00e-04, 3.00e-04, 3.00e-04, \
                       2.00e-04, 2.00e-04, 1.00e-04, 1.00e-04, 0.00e+00, \
                       0.00e+00]

    filtsize = [24, 21, 24, 24, 23, 47, 89, 75, 89, 141]
#		Holds the filter zero-points as determined from
#		Vega model by Dreiling & Bell (ApJ, 241,736, 1980)
#
#		B	6.268e-9   erg cm-2 s-1 A-1
#		V	3.604e-9
#		R	2.161e-9
#		I	1.126e-9
#
#		The following zero-points are from Lamla
#		(Landolt-Boernstein Vol. 2b, eds. K. Schaifer & 
#		H.H. Voigt, Berlin: Springer, p. 73, 1982 QC61.L332)
#
#		U	4.22e-9   erg cm-2 s-1 A-1
#
#		J	3.1e-10
#		H	1.2e-10
#		K	3.9e-11
#
#               U        B          V        R         I
    zp_johnson = np.array([4.22e-9, 6.268e-9, 3.604e-9, 2.161e-9, 1.126e-9])
    leff_sloan=np.array([3560.,  4830.,  6260.,  7670.,  9100])
    zp_sloan=3.631e-20*2.99792458e18/(leff_sloan*leff_sloan)
    zeropoint=np.concatenate([zp_johnson,zp_sloan])
    mag=np.zeros(10)
    filtflux=mag.copy()
    coverage=mag.copy()
    efflambda=mag.copy()
    totflux=mag.copy()
    filtername = ['U', 'B', 'V', 'R', 'I','u','g','r','i','z']
    for i,_ in enumerate(filtername):
        filtw=filtwave[0:filtsize[i],i]
        filtt=filttran[0:filtsize[i],i]
        mag[i], filtflux[i], coverage[i], efflambda[i], totflux[i]= \
              filtermag(hop[0].wave,flux, filtw, filtt, \
              zeropoint[i])                                                            
    logging.info('For object {}'.format(hop[0].obname))
    logging.info('Filter magnitude  Flux(erg/s/cm^2/A) Flux(erg/s/cm^2)  Coverage(%)  Eff. Lambda')
    for i in range(0,5):
        if (mag[i] > 99):
            logging.info('  {:1s}        FILTER AND SPECTRUM DO NOT OVERLAP'.format(filtername[i]))
        else:
            logging.info('  {:1s}     {:6.3f}      {:10.4e}        {:10.4e}         {:5.1f}         {:6.1f}'.format(filtername[i],mag[i],filtflux[i],totflux[i],coverage[i]*100.,efflambda[i]))

    for i in range(5,10):
        if (mag[i] > 99):
            logging.info('  {:1s}        FILTER AND SPECTRUM DO NOT OVERLAP'.format(filtername[i]))
        else:
            logging.info('  {:1s}     {:6.3f}      {:10.4e}        {:10.4e}         {:5.1f}         {:6.1f}'.format(filtername[i],mag[i],filtflux[i],totflux[i],coverage[i]*100.,efflambda[i]))

            
    print(' ')
    logging.info('Colors')
    colortab=[[0,1],[1,2],[2,3],[2,4],[5,6],[6,7],[7,8],[8,9]]
    for i in range(0,4):
        if (mag[colortab[i][0]] > 99) or (mag[colortab[i][1]] > 99):
            logging.info('{}-{}    ONE OR BOTH FILTERS DO NOT OVERLAP SPECTRUM'.format(filtername[colortab[i][0]],filtername[colortab[i][1]]))
        else:
            logging.info('{:1s}-{:1s}    {:12.4f}'.format(filtername[colortab[i][0]],filtername[colortab[i][1]],mag[colortab[i][0]]-mag[colortab[i][1]]))
    for i in range(4,8):
        if (mag[colortab[i][0]] > 99) or (mag[colortab[i][1]] > 99):
            logging.info('{}-{}    ONE OR BOTH FILTERS DO NOT OVERLAP SPECTRUM'.format(filtername[colortab[i][0]],filtername[colortab[i][1]]))
        else:
            logging.info('{:1s}-{:1s}    {:12.4f}'.format(filtername[colortab[i][0]],filtername[colortab[i][1]],mag[colortab[i][0]]-mag[colortab[i][1]]))

    print('\nWould you like to scale the spectrum to match photometry?\n')
    answer=yesno('n')
    if (answer == 'y'):
        print('\nWhich filter do you have?')
        scalefilt=inputter_single_mix('U/B/V/R/I/u/g/r/i/z: ','UBVRIugriz')
        filtindex=filtername.index(scalefilt)
        scalemag=inputter('Enter your value for filter {}: '.format(filtername[filtindex]),'float',False)
        print(' ')
        logging.info('Scaling {} from {}={:6.3f} to {}={}'.format(hop[0].obname,filtername[filtindex],mag[filtindex],filtername[filtindex],scalemag))
        logging.info('Multiplying by {:.3f}'.format(10**(0.4*(mag[filtindex]-scalemag))))
        hop[0].flux=hop[0].flux*10**(0.4*(mag[filtindex]-scalemag))
    

    return hop


