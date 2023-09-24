# BallDetecton2.0
<br />Color-Based Object Detection:<br />
 <br />It defines color ranges in the HSV color space for Dark Blue PANTONE 2727 C and purple Pantone 7655C.<br />
 <br />It captures video from a webcam and applies color filtering to isolate regions matching these colors.<br />
 
<br />Ball Size Estimation:<br />
 <br />It estimates the size of detected balls based on their contour areas, assuming a circular shape and calculating the equivalent diameter.<br />
 vVisualization and Annotation:<br />

<br />It visually annotates the detected balls:<br />
<br /> Draws contours around the balls with appropriate colors (blue or purple).<br />
 <br />Places a dot at the center of each detected ball.<br />
<br /> Writes "Blue" or "Purple" near the respective balls.<br />
 
<br />Distance Calculation:<br />
<br /> It calculates an estimated distance from the camera to each ball based on the assumed ball diameter and the camera's focal length.<br />

<br />User Interaction:<br />
 <br />The code aims to detect balls of specific colors and sizes in real-time using a webcam. <br />
 <br />It provides visual feedback by annotating the detected balls and estimating their distances from the camera based on specified assumptions. <br />
<br /> Keep in mind that the accuracy of the size estimation and distance calculation is based on assumptions and should be adjusted based on actual camera properties and real-world conditions.<br />
