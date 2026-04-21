///////////////////////////////////////////////////////////////////////////////
// viewmanager.h
// ============
// manage the viewing of 3D objects within the viewport
//
//  AUTHOR: Brian Battersby - SNHU Instructor / Computer Science
//	Created for CS-330-Computational Graphics and Visualization, Nov. 1st, 2023
///////////////////////////////////////////////////////////////////////////////

#include "ViewManager.h"

// GLM Math Header inclusions
#include <glm/glm.hpp>
#include <glm/gtx/transform.hpp>
#include <glm/gtc/type_ptr.hpp>    

// declaration of the global variables and defines
namespace
{
	// Variables for window width and height
	const int WINDOW_WIDTH = 1000;
	const int WINDOW_HEIGHT = 800;
	const char* g_ViewName = "view";
	const char* g_ProjectionName = "projection";

	// camera object used for viewing and interacting with
	// the 3D scene
	Camera* g_pCamera = nullptr;

	// these variables are used for mouse movement processing
	float gLastX = WINDOW_WIDTH / 2.0f;
	float gLastY = WINDOW_HEIGHT / 2.0f;
	bool gFirstMouse = true;

	//Milestone3: Added Mouse Movement tracking for Camera orientation
	const float MOUSE_SENSITIVITY_SCALE = 3.00f;					//Note: Change this sensitivity to increase mouse cursor camera movement speed

	//Milestone3: Added Movement Speed variable
	float gMoveSpeed = 6.0f;

	// time between current frame and last frame
	float gDeltaTime = 0.0f; 
	float gLastFrame = 0.0f;

	// the following variable is false when orthographic projection
	// is off and true when it is on
	bool bOrthographicProjection = false;
}

/***********************************************************
 *  ViewManager()
 *
 *  The constructor for the class
 ***********************************************************/
ViewManager::ViewManager(
	ShaderManager *pShaderManager)
{
	// initialize the member variables
	m_pShaderManager = pShaderManager;
	m_pWindow = NULL;
	g_pCamera = new Camera();
	// default camera view parameters
	g_pCamera->Position = glm::vec3(0.0f, 5.0f, 12.0f);
	g_pCamera->Front = glm::vec3(0.0f, -0.5f, -2.0f);
	g_pCamera->Up = glm::vec3(0.0f, 1.0f, 0.0f);
	g_pCamera->Zoom = 80;
}

/***********************************************************
 *  ~ViewManager()
 *
 *  The destructor for the class
 ***********************************************************/
ViewManager::~ViewManager()
{
	// free up allocated memory
	m_pShaderManager = NULL;
	m_pWindow = NULL;
	if (NULL != g_pCamera)
	{
		delete g_pCamera;
		g_pCamera = NULL;
	}
}

/***********************************************************
 *  CreateDisplayWindow()
 *
 *  This method is used to create the main display window.
 ***********************************************************/
GLFWwindow* ViewManager::CreateDisplayWindow(const char* windowTitle)
{
	GLFWwindow* window = nullptr;

	// try to create the displayed OpenGL window
	window = glfwCreateWindow(
		WINDOW_WIDTH,
		WINDOW_HEIGHT,
		windowTitle,
		NULL, NULL);
	if (window == NULL)
	{
		std::cout << "Failed to create GLFW window" << std::endl;
		glfwTerminate();
		return NULL;
	}
	glfwMakeContextCurrent(window);

	// tell GLFW to capture all mouse events
	//glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);

	// this callback is used to receive mouse moving events
	glfwSetCursorPosCallback(window, &ViewManager::Mouse_Position_Callback);
	//Milestone3: Added mouse scroll callback
	glfwSetScrollCallback(window, &ViewManager::Mouse_Scroll_Callback);

	// enable blending for supporting tranparent rendering
	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

	m_pWindow = window;

	return(window);
}

/***********************************************************
 *  Mouse_Position_Callback()
 *
 *  This method is automatically called from GLFW whenever
 *  the mouse is moved within the active GLFW display window.
 ***********************************************************/


//Milestone 3: Convert mouse delta movement into Camera yaw/pitch updates
//Enables 3D looking around the scene.
void ViewManager::Mouse_Position_Callback(GLFWwindow* window, double xMousePos, double yMousePos)
{
	if (NULL == g_pCamera)				//If camera does not exist, do nothing.
	{
		return;
	}

	if (gFirstMouse)				//On first mouse event, initialize last-known cursor position.
	{
		gLastX = (float)xMousePos;
		gLastY = (float)yMousePos;
		gFirstMouse = false;
		return;
	}

	float xOffset = (float)xMousePos - gLastX;		//Movement calculations
	float yOffset = gLastY - (float)yMousePos;

	gLastX = (float)xMousePos;						//Position calculations
	gLastY = (float)yMousePos;

	xOffset *= MOUSE_SENSITIVITY_SCALE;				//Offset scaling for smooth mouse movement
	yOffset *= MOUSE_SENSITIVITY_SCALE;

	g_pCamera->ProcessMouseMovement(xOffset, yOffset);	//Move movement control to mouse
}

/***********************************************************
 *  Mouse_Scroll_Callback()
 *
 *  This method is automatically called from GLFW whenever the mouse scroll wheel is moved.
 *  The scroll wheel adjusts the camera's movement speed.
 ***********************************************************/
void ViewManager::Mouse_Scroll_Callback(GLFWwindow* window, double xOffset, double yOffset)
{
	if (NULL == g_pCamera)			//If camera does not exist, do nothing
	{
		return;
	}

	gMoveSpeed += (float)yOffset;	// Adjust movement speed based on scroll direction

	if (gMoveSpeed < 1.0f)			//Restrict speeds to useful ranges, prevents over tuning.
	{
		gMoveSpeed = 1.0f;
	}
	if (gMoveSpeed > 20.0f)
	{
		gMoveSpeed = 20.0f;
	}
}


/***********************************************************
 *  ProcessKeyboardEvents()
 *
 *  This method is called to process any keyboard events
 *  that may be waiting in the event queue.
 ***********************************************************/
void ViewManager::ProcessKeyboardEvents()
{
	// close the window if the escape key has been pressed
	if (glfwGetKey(m_pWindow, GLFW_KEY_ESCAPE) == GLFW_PRESS)
	{
		glfwSetWindowShouldClose(m_pWindow, true);
	}

	//Milestone 3: Projection Toggle Keys added. Enables swapping between Orthographic (2D) and perspective (3D) views.

	if (glfwGetKey(m_pWindow, GLFW_KEY_P) == GLFW_PRESS)		//P switches to Perspective view
	{
		bOrthographicProjection = false;
	}

	if (glfwGetKey(m_pWindow, GLFW_KEY_O) == GLFW_PRESS)		//O switches to Orthographic view.
	{
		bOrthographicProjection = true;
	}

	//Milestone 3: Added Keyboard movement capabilities
	if (NULL == g_pCamera)				//If the camera object is null, then exit this method
	{
		return;
	}

	// Basic camera navigation (WASD + QE)

	if (glfwGetKey(m_pWindow, GLFW_KEY_W) == GLFW_PRESS)	//WS controlling Forward and Backward (depth)
	{
		g_pCamera->ProcessKeyboard(FORWARD, gDeltaTime * gMoveSpeed);
	}
	if (glfwGetKey(m_pWindow, GLFW_KEY_S) == GLFW_PRESS)
	{
		g_pCamera->ProcessKeyboard(BACKWARD, gDeltaTime * gMoveSpeed);
	}

	if (glfwGetKey(m_pWindow, GLFW_KEY_A) == GLFW_PRESS)	//AD controlling Left and Right (Horizontal)
	{
		g_pCamera->ProcessKeyboard(LEFT, gDeltaTime * gMoveSpeed);
	}
	if (glfwGetKey(m_pWindow, GLFW_KEY_D) == GLFW_PRESS)
	{
		g_pCamera->ProcessKeyboard(RIGHT, gDeltaTime * gMoveSpeed);
	}

	if (glfwGetKey(m_pWindow, GLFW_KEY_E) == GLFW_PRESS)		//EQ controlling Up and Down (Vertical)
	{
		g_pCamera->Position += (g_pCamera->Up * gDeltaTime);
	}
	if (glfwGetKey(m_pWindow, GLFW_KEY_Q) == GLFW_PRESS)
	{
		g_pCamera->Position -= (g_pCamera->Up * gDeltaTime);
	}
}

/***********************************************************
 *  PrepareSceneView()
 *
 *  This method is used for preparing the 3D scene by loading
 *  the shapes, textures in memory to support the 3D scene 
 *  rendering
 ***********************************************************/
void ViewManager::PrepareSceneView()
{
	glm::mat4 view;
	glm::mat4 projection;

	// per-frame timing
	float currentFrame = glfwGetTime();
	gDeltaTime = currentFrame - gLastFrame;
	gLastFrame = currentFrame;

	// process any keyboard events that may be waiting in the 
	// event queue
	ProcessKeyboardEvents();

	// get the current view matrix from the camera
	view = g_pCamera->GetViewMatrix();

	//Milestone 3: Modified Projection matrix to dynamically switch projection matrices.
	
	if (bOrthographicProjection)
	{
		const glm::vec3 targetPos = glm::vec3(6.0f, 5.0f, 1.5f);		//Orthographic (2D) projection

		g_pCamera->Position = glm::vec3(targetPos.x, targetPos.y, targetPos.z + 20.0f);		//Align the camera to X and Z, and set Y to target
		g_pCamera->Front = glm::normalize(targetPos - g_pCamera->Position);

		g_pCamera->Up = glm::vec3(0.0f, 1.0f, 0.0f);				//Steady camera

		projection = glm::ortho(					//Set the location of the camera when going into Orthographic view.
			-10.0f, 10.0f,   // left, right
			-10.0f, 10.0f,   // bottom, top
			0.1f, 100.0f     // near, far
		);
	}
	else
	{
		projection = glm::perspective(							//Perspective (3D) projection
			glm::radians(g_pCamera->Zoom),
			(GLfloat)WINDOW_WIDTH / (GLfloat)WINDOW_HEIGHT,
			0.1f, 100.0f
		);
	}


	// if the shader manager object is valid
	if (NULL != m_pShaderManager)
	{
		// set the view matrix into the shader for proper rendering
		m_pShaderManager->setMat4Value(g_ViewName, view);
		// set the view matrix into the shader for proper rendering
		m_pShaderManager->setMat4Value(g_ProjectionName, projection);
		// set the view position of the camera into the shader for proper rendering
		m_pShaderManager->setVec3Value("viewPosition", g_pCamera->Position);
	}
}