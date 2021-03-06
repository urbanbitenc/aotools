"""
A library of functions which may be of use to analyse WFS data
"""

def r0fromSlopes(slopes, wavelength, subapDiam):
    """
    Measures the value of R0 from a set of WFS slopes.
    
    Uses the equation in Saint Jaques, 1998, PhD Thesis, Appendix A to calculate the value of atmospheric seeing parameter, r0, that would result in the variance of the given slopes. The slopes should represent only the X or Y directions.

    Parameters:
        slopes (ndarray): A 3-d set of slopes in radians, of shape (dimension, nSubaps, nFrames)
        wavelength (float): The wavelegnth of the light observed
        subapDiam (float) The diameter of each sub-aperture

    Returns:
        float: An estimate of r0 for that dataset.

    """
    slopeVar = slopes.var(axis=(-1))

    r0 = ((0.162*(wavelength**2) * subapDiam**(-1./3)) / slopeVar)**(3./5)
    
    r0 = r0.mean()

    return r0