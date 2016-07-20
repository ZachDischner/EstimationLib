// KalmanFilter
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
#ifndef KALMANFILTER_H     // Prevent duplicate definition
#define KALMANFILTER_H

// Includes  
#include <string.h>

class KalmanFilter
{
    public:
        // Constructor
        KalmanFilter();

        // Deconstructor
        ~KalmanFilter()

        // Public Functions
        int doSomething(int var);
}