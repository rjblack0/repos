///////////////////////////////////////////////////////////////////////////////
// shadermanager.cpp
// ============
// manage the loading and rendering of 3D scenes
//
//  AUTHOR: Brian Battersby - SNHU Instructor / Computer Science
//	Created for CS-330-Computational Graphics and Visualization, Nov. 1st, 2023
///////////////////////////////////////////////////////////////////////////////

#include "SceneManager.h"

#ifndef STB_IMAGE_IMPLEMENTATION
#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#endif

#include <glm/gtx/transform.hpp>

// declaration of global variables
namespace
{
	const char* g_ModelName = "model";
	const char* g_ColorValueName = "objectColor";
	const char* g_TextureValueName = "objectTexture";
	const char* g_UseTextureName = "bUseTexture";
	const char* g_UseLightingName = "bUseLighting";

	// -----------------------------
	// Scene constants
	// -----------------------------
	const glm::vec3 TABLE_SCALE = glm::vec3(20.0f, 1.0f, 10.0f);
	const glm::vec3 TABLE_POS = glm::vec3(0.0f, 0.0f, 0.0f);
	const glm::vec4 TABLE_COLOR = glm::vec4(0.12f, 0.12f, 0.12f, 1.0f);

	// Thermos anchor and orientation
	const float THERMOS_X = 6.0f;
	const float THERMOS_Z = 1.5f;
	const float THERMOS_BASE_Y = 0.15f;
	const float THERMOS_YAW = -15.0f;

	// Thermos dimensions
	const glm::vec3 THERMOS_BODY_SCALE = glm::vec3(1.6f, 7.0f, 1.6f);
	const glm::vec3 THERMOS_BAND_SCALE = glm::vec3(1.75f, 1.0f, 1.75f);
	const glm::vec3 THERMOS_CAP_SCALE = glm::vec3(1.6f, 1.6f, 1.6f);
	const glm::vec3 THERMOS_RING_SCALE = glm::vec3(1.7f, 0.6f, 1.7f);

	// Thermos colors
	const glm::vec4 THERMOS_BODY_COLOR = glm::vec4(0.06f, 0.06f, 0.06f, 1.0f);
	const glm::vec4 THERMOS_BAND_COLOR = glm::vec4(0.08f, 0.08f, 0.08f, 1.0f);
	const glm::vec4 THERMOS_CAP_COLOR = glm::vec4(0.78f, 0.78f, 0.80f, 1.0f);
	const glm::vec4 THERMOS_RING_COLOR = glm::vec4(0.04f, 0.04f, 0.04f, 1.0f);

	// Stacking offsets
	const float BODY_HEIGHT = THERMOS_BODY_SCALE.y;
	const float BAND_HEIGHT = THERMOS_BAND_SCALE.y;

}

/***********************************************************
 *  SceneManager()
 *
 *  The constructor for the class
 ***********************************************************/
SceneManager::SceneManager(ShaderManager* pShaderManager)
{
	m_pShaderManager = pShaderManager;
	m_basicMeshes = new ShapeMeshes();
	m_loadedTextures = 0;
}

/***********************************************************
 *  ~SceneManager()
 *
 *  The destructor for the class
 ***********************************************************/
SceneManager::~SceneManager()
{
	m_pShaderManager = nullptr;
	delete m_basicMeshes;
	m_basicMeshes = NULL;
}

/***********************************************************
 *  CreateGLTexture()
 *
 *  This method is used for loading textures from image files,
 *  configuring the texture mapping parameters in OpenGL,
 *  generating the mipmaps, and loading the read texture into
 *  the next available texture slot in memory.
 ***********************************************************/
bool SceneManager::CreateGLTexture(const char* filename, std::string tag)
{
	int width = 0;
	int height = 0;
	int colorChannels = 0;
	GLuint textureID = 0;

	// indicate to always flip images vertically when loaded
	stbi_set_flip_vertically_on_load(true);

	// try to parse the image data from the specified image file
	unsigned char* image = stbi_load(
		filename,
		&width,
		&height,
		&colorChannels,
		0);

	// if the image was successfully read from the image file
	if (image)
	{
		std::cout << "Successfully loaded image:" << filename << ", width:" << width << ", height:" << height << ", channels:" << colorChannels << std::endl;

		glGenTextures(1, &textureID);
		glBindTexture(GL_TEXTURE_2D, textureID);

		// set the texture wrapping parameters
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
		// set texture filtering parameters
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

		// if the loaded image is in RGB format
		if (colorChannels == 3)
			glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB8, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image);
		// if the loaded image is in RGBA format - it supports transparency
		else if (colorChannels == 4)
			glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image);
		else
		{
			std::cout << "Not implemented to handle image with " << colorChannels << " channels" << std::endl;
			return false;
		}

		// generate the texture mipmaps for mapping textures to lower resolutions
		glGenerateMipmap(GL_TEXTURE_2D);

		// free the image data from local memory
		stbi_image_free(image);
		glBindTexture(GL_TEXTURE_2D, 0); // Unbind the texture

		// register the loaded texture and associate it with the special tag string
		m_textureIDs[m_loadedTextures].ID = textureID;
		m_textureIDs[m_loadedTextures].tag = tag;
		m_loadedTextures++;

		return true;
	}

	std::cout << "Could not load image:" << filename << std::endl;

	// Error loading the image
	return false;
}

/***********************************************************
 *  BindGLTextures()
 *
 *  This method is used for binding the loaded textures to
 *  OpenGL texture memory slots.  There are up to 16 slots.
 ***********************************************************/
void SceneManager::BindGLTextures()
{
	for (int i = 0; i < m_loadedTextures; i++)
	{
		// bind textures on corresponding texture units
		glActiveTexture(GL_TEXTURE0 + i);
		glBindTexture(GL_TEXTURE_2D, m_textureIDs[i].ID);
	}
}

/***********************************************************
 *  DestroyGLTextures()
 *
 *  This method is used for freeing the memory in all the
 *  used texture memory slots.
 ***********************************************************/
void SceneManager::DestroyGLTextures()
{
	for (int i = 0; i < m_loadedTextures; i++)
	{
		glGenTextures(1, &m_textureIDs[i].ID);
	}
}

/***********************************************************
 *  FindTextureID()
 *
 *  This method is used for getting an ID for the previously
 *  loaded texture bitmap associated with the passed in tag.
 ***********************************************************/
int SceneManager::FindTextureID(std::string tag)
{
	int textureID = -1;
	int index = 0;
	bool bFound = false;

	while ((index < m_loadedTextures) && (bFound == false))
	{
		if (m_textureIDs[index].tag.compare(tag) == 0)
		{
			textureID = m_textureIDs[index].ID;
			bFound = true;
		}
		else
			index++;
	}

	return(textureID);
}

/***********************************************************
 *  FindTextureSlot()
 *
 *  This method is used for getting a slot index for the previously
 *  loaded texture bitmap associated with the passed in tag.
 ***********************************************************/
int SceneManager::FindTextureSlot(std::string tag)
{
	int textureSlot = -1;
	int index = 0;
	bool bFound = false;

	while ((index < m_loadedTextures) && (bFound == false))
	{
		if (m_textureIDs[index].tag.compare(tag) == 0)
		{
			textureSlot = index;
			bFound = true;
		}
		else
			index++;
	}

	return(textureSlot);
}

/***********************************************************
 *  FindMaterial()
 *
 *  This method is used for getting a material from the previously
 *  defined materials list that is associated with the passed in tag.
 ***********************************************************/
bool SceneManager::FindMaterial(std::string tag, OBJECT_MATERIAL& material)
{
	if (m_objectMaterials.size() == 0)
	{
		return(false);
	}

	int index = 0;
	bool bFound = false;
	while ((index < m_objectMaterials.size()) && (bFound == false))
	{
		if (m_objectMaterials[index].tag.compare(tag) == 0)
		{
			bFound = true;
			material.ambientColor = m_objectMaterials[index].ambientColor;
			material.ambientStrength = m_objectMaterials[index].ambientStrength;
			material.diffuseColor = m_objectMaterials[index].diffuseColor;
			material.specularColor = m_objectMaterials[index].specularColor;
			material.shininess = m_objectMaterials[index].shininess;
		}
		else
		{
			index++;
		}
	}

	return(true);
}

/***********************************************************
 *  SetTransformations()
 *
 *  This method is used for setting the transform buffer
 *  using the passed in transformation values.
 ***********************************************************/
void SceneManager::SetTransformations(
	glm::vec3 scaleXYZ,
	float XrotationDegrees,
	float YrotationDegrees,
	float ZrotationDegrees,
	glm::vec3 positionXYZ)
{
	// variables for this method
	glm::mat4 modelView;
	glm::mat4 scale;
	glm::mat4 rotationX;
	glm::mat4 rotationY;
	glm::mat4 rotationZ;
	glm::mat4 translation;

	// set the scale value in the transform buffer
	scale = glm::scale(scaleXYZ);
	// set the rotation values in the transform buffer
	rotationX = glm::rotate(glm::radians(XrotationDegrees), glm::vec3(1.0f, 0.0f, 0.0f));
	rotationY = glm::rotate(glm::radians(YrotationDegrees), glm::vec3(0.0f, 1.0f, 0.0f));
	rotationZ = glm::rotate(glm::radians(ZrotationDegrees), glm::vec3(0.0f, 0.0f, 1.0f));
	// set the translation value in the transform buffer
	translation = glm::translate(positionXYZ);

	modelView = translation * rotationX * rotationY * rotationZ * scale;

	if (m_pShaderManager != nullptr)
	{
		m_pShaderManager->setMat4Value(g_ModelName, modelView);
	}
}

/***********************************************************
 *  SetShaderColor()
 *
 *  This method is used for setting the passed in color
 *  into the shader for the next draw command
 ***********************************************************/
void SceneManager::SetShaderColor(
	float redColorValue,
	float greenColorValue,
	float blueColorValue,
	float alphaValue)
{
	// variables for this method
	glm::vec4 currentColor;

	currentColor.r = redColorValue;
	currentColor.g = greenColorValue;
	currentColor.b = blueColorValue;
	currentColor.a = alphaValue;

	if (NULL != m_pShaderManager)
	{
		m_pShaderManager->setIntValue(g_UseTextureName, false);
		m_pShaderManager->setVec4Value(g_ColorValueName, currentColor);
	}
}

/***********************************************************
 *  SetShaderTexture()
 *
 *  This method is used for setting the texture data
 *  associated with the passed in ID into the shader.
 ***********************************************************/
void SceneManager::SetShaderTexture(
	std::string textureTag)
{
	if (NULL != m_pShaderManager)
	{
		m_pShaderManager->setIntValue(g_UseTextureName, true);

		int textureID = -1;
		textureID = FindTextureSlot(textureTag);
		m_pShaderManager->setSampler2DValue(g_TextureValueName, textureID);
	}
}

/***********************************************************
 *  SetTextureUVScale()
 *
 *  This method is used for setting the texture UV scale
 *  values into the shader.
 ***********************************************************/
void SceneManager::SetTextureUVScale(float u, float v)
{
	if (NULL != m_pShaderManager)
	{
		m_pShaderManager->setVec2Value("UVscale", glm::vec2(u, v));
	}
}

/***********************************************************
 *  SetShaderMaterial()
 *
 *  This method is used for passing the material values
 *  into the shader.
 ***********************************************************/
void SceneManager::SetShaderMaterial(
	std::string materialTag)
{
	if (m_objectMaterials.size() > 0)
	{
		OBJECT_MATERIAL material;
		bool bReturn = false;

		bReturn = FindMaterial(materialTag, material);
		if (bReturn == true)
		{
			m_pShaderManager->setVec3Value("material.ambientColor", material.ambientColor);
			m_pShaderManager->setFloatValue("material.ambientStrength", material.ambientStrength);
			m_pShaderManager->setVec3Value("material.diffuseColor", material.diffuseColor);
			m_pShaderManager->setVec3Value("material.specularColor", material.specularColor);
			m_pShaderManager->setFloatValue("material.shininess", material.shininess);
		}
	}
}

/**************************************************************/
/*** STUDENTS CAN MODIFY the code in the methods BELOW for  ***/
/*** preparing and rendering their own 3D replicated scenes.***/
/*** Please refer to the code in the OpenGL sample project  ***/
/*** for assistance.                                        ***/
/**************************************************************/

// Milestone Two refactor after feedback. Using helper functions + constants to reduce cognitive load in RenderScene()
// Minimize "magic numbers" for easier future changes


void SceneManager::RenderTable()
{
	glm::vec3 scaleXYZ = TABLE_SCALE;
	glm::vec3 positionXYZ = TABLE_POS;

	float XrotationDegrees = 0.0f;
	float YrotationDegrees = 0.0f;
	float ZrotationDegrees = 0.0f;

	SetTransformations(scaleXYZ, XrotationDegrees, YrotationDegrees, ZrotationDegrees, positionXYZ);
	SetShaderColor(TABLE_COLOR.r, TABLE_COLOR.g, TABLE_COLOR.b, TABLE_COLOR.a);

	//Milestone 5: Added texture so that plane will reflect light

	//Added wood texture.

	SetShaderColor(1.0f, 1.0f, 1.0f, 1.0f);
	SetShaderTexture("rusticwood");
	SetTextureUVScale(3.0f, 3.0f);

	SetShaderMaterial("table");

	m_basicMeshes->DrawPlaneMesh();
}

void SceneManager::RenderThermos()
{
	//Thermos anchor
	const glm::vec3 thermosAnchor = glm::vec3(THERMOS_X, THERMOS_BASE_Y, THERMOS_Z);

	// Shared rotation for all thermos pieces
	const float XrotationDegrees = 0.0f;
	const float YrotationDegrees = THERMOS_YAW;
	const float ZrotationDegrees = 0.0f;

	//Changed to White so textures are not tinted
	const glm::vec4 WHITE = glm::vec4(1.0f, 1.0f, 1.0f, 1.0f);

	//Milestone 4:
	SetTransformations(THERMOS_BODY_SCALE, XrotationDegrees, YrotationDegrees, ZrotationDegrees, thermosAnchor);
	
	// Milestone 4 Complex Technique: Tile the body texture vertically for added detail.
	
	//Base

	//Milestone 5: Added Shader Material call.
	SetShaderMaterial("thermosbody");

	SetShaderColor(WHITE.r, WHITE.g, WHITE.b, WHITE.a);
	SetShaderTexture("thermosbase");
	SetTextureUVScale(1.0f, 2.0f);

	m_basicMeshes->DrawCylinderMesh();

	// Upper band
	glm::vec3 bandPos = thermosAnchor + glm::vec3(0.0f, BODY_HEIGHT, 0.0f);
	SetTransformations(THERMOS_BAND_SCALE, XrotationDegrees, YrotationDegrees, ZrotationDegrees, bandPos);

	//Milestone 5: Added Shader Material call.
	SetShaderMaterial("thermosbody");

	SetShaderColor(WHITE.r, WHITE.g, WHITE.b, WHITE.a);
	SetShaderTexture("thermosbase");
	SetTextureUVScale(1.0f, 0.3f);

	m_basicMeshes->DrawCylinderMesh();

	//Cap
	glm::vec3 capPos = thermosAnchor + glm::vec3(0.0f, BODY_HEIGHT + BAND_HEIGHT, 0.0f);
	SetTransformations(THERMOS_CAP_SCALE, XrotationDegrees, YrotationDegrees, ZrotationDegrees, capPos);

	//Milestone 5: Added Shader Material call.
	SetShaderMaterial("stainless");

	SetShaderColor(WHITE.r, WHITE.g, WHITE.b, WHITE.a);
	SetShaderTexture("stainless");
	SetTextureUVScale(1.0f, 1.0f);

	m_basicMeshes->DrawTaperedCylinderMesh();

	//Bottom ring

	SetTransformations(THERMOS_RING_SCALE, XrotationDegrees, YrotationDegrees, ZrotationDegrees, thermosAnchor);


	//Milestone 5: Added Shader Material call.
	SetShaderMaterial("table");

	SetShaderColor(WHITE.r, WHITE.g, WHITE.b, WHITE.a);
	SetShaderTexture("rusticwood");
	SetTextureUVScale(1.0f, 2.0f);

	m_basicMeshes->DrawCylinderMesh();

}

//Final Project: Added Book, Tin, Bowl

void SceneManager::RenderBook()
{
	// Overall book size
	glm::vec3 bookScale(3.0f, 1.8f, 3.5f);

	const float BOOK_OFFSET_X = -12.0f;
	const float BOOK_OFFSET_Z = 1.5f;

	glm::vec3 bookCenter(
		THERMOS_X + BOOK_OFFSET_X,
		(bookScale.y * 0.5f),
		THERMOS_Z + BOOK_OFFSET_Z
	);

	//Same rotation for all parts
	const float rotX = 0.0f;
	const float rotY = 0.0f;
	const float rotZ = 0.0f;

	//Split thickness into cover, pages, cover
	const float coverThickness = bookScale.y * 0.15f;
	const float pagesThickness = bookScale.y - (coverThickness * 2.0f);

	//Pages inset so covers “wrap” them a little
	glm::vec3 pagesScale(bookScale.x * 0.94f, pagesThickness, bookScale.z * 0.94f);

	//Compute Y positions for stacked slabs
	const float bottomY = bookCenter.y - (bookScale.y * 0.5f) + (coverThickness * 0.5f);
	const float pagesY = bottomY + (coverThickness * 0.5f) + (pagesThickness * 0.5f);
	const float topY = pagesY + (pagesThickness * 0.5f) + (coverThickness * 0.5f);
	const float spineThickness = 0.35f;

	//Bottom cover
	{
		glm::vec3 coverScale(bookScale.x, coverThickness, bookScale.z);
		glm::vec3 coverPos(bookCenter.x, bottomY, bookCenter.z);

		SetTransformations(coverScale, rotX, rotY, rotZ, coverPos);
		SetShaderColor(1, 1, 1, 1);
		SetShaderTexture("book");
		SetTextureUVScale(1.0f, 1.0f);
		SetShaderMaterial("table");
		m_basicMeshes->DrawBoxMesh();
	}

	//Pages
	{
		glm::vec3 pagesPos(bookCenter.x, pagesY, bookCenter.z);

		SetTransformations(pagesScale, rotX, rotY, rotZ, pagesPos);
		SetShaderColor(1, 1, 1, 1);
		SetShaderTexture("paper");
		SetTextureUVScale(1.0f, 1.0f);
		SetShaderMaterial("table");
		m_basicMeshes->DrawBoxMesh();
	}

	//Top cover
	{
		glm::vec3 coverScale(bookScale.x, coverThickness, bookScale.z);
		glm::vec3 coverPos(bookCenter.x, topY, bookCenter.z);

		SetTransformations(coverScale, rotX, rotY, rotZ, coverPos);
		SetShaderColor(1, 1, 1, 1);
		SetShaderTexture("book");
		SetTextureUVScale(1.0f, 1.0f);
		SetShaderMaterial("table");
		m_basicMeshes->DrawBoxMesh();
	}

	//Spine
	{
		const float spineThickness = 0.35f; //x thickness of the spine

		glm::vec3 spineScale(spineThickness, bookScale.y, bookScale.z);

		glm::vec3 spinePos(
			bookCenter.x - (bookScale.x * 0.5f) + (spineScale.x * 0.5f) - 0.01f,
			bookCenter.y,
			bookCenter.z
		);

		SetTransformations(spineScale, rotX, rotY, rotZ, spinePos);
		SetShaderColor(1, 1, 1, 1);
		SetShaderTexture("book");
		SetTextureUVScale(1.0f, 1.0f);
		SetShaderMaterial("table");
		m_basicMeshes->DrawBoxMesh();
	}
}

void SceneManager::RenderTin()
{
	glm::vec3 bodyScale(5.0f, 3.0f, 4.0f);

	const float TIN_OFFSET_X = -6.0f;
	const float TIN_OFFSET_Z = -4.5f;

	glm::vec3 bodyCenter(
		THERMOS_X + TIN_OFFSET_X,
		(bodyScale.y * 0.5f),
		THERMOS_Z + TIN_OFFSET_Z
	);

	const float rotX = 0.0f;
	const float rotY = 0.0f;
	const float rotZ = 0.0f;

	//Body
	SetTransformations(bodyScale, rotX, rotY, rotZ, bodyCenter);
	SetShaderColor(1, 1, 1, 1);
	SetShaderTexture("stainless_red");
	SetTextureUVScale(1.0f, 1.0f);
	SetShaderMaterial("stainless");
	m_basicMeshes->DrawBoxMesh();


	//Lid
	const float lidThickness = 0.4f;

	glm::vec3 lidScale(
		bodyScale.x * 1.05f,   //slight overhang
		lidThickness,
		bodyScale.z * 1.05f
	);

	glm::vec3 lidCenter(
		bodyCenter.x,
		bodyCenter.y + (bodyScale.y * 0.5f) + (lidThickness * 0.5f),
		bodyCenter.z
	);

	SetTransformations(lidScale, rotX, rotY, rotZ, lidCenter);
	SetShaderColor(1, 1, 1, 1);
	SetShaderTexture("gold");
	SetTextureUVScale(1.0f, 1.0f);
	SetShaderMaterial("stainless");
	m_basicMeshes->DrawBoxMesh();
}

void SceneManager::RenderBowl()
{
	const float BOWL_OFFSET_X = -6.0f;
	const float BOWL_OFFSET_Z = 1.5f;

	glm::vec3 bowlCenter(
		THERMOS_X + BOWL_OFFSET_X,
		0.55f,
		THERMOS_Z + BOWL_OFFSET_Z
	);

	//Outer bowl
	glm::vec3 outerScale(2.2f, 1.1f, 2.2f);
	SetTransformations(outerScale, 0.0f, 0.0f, 0.0f, bowlCenter);

	SetShaderColor(1.0f, 1.0f, 1.0f, 1.0f);
	SetShaderTexture("backdrop");
	SetTextureUVScale(1.0f, 1.0f);
	SetShaderMaterial("stainless");
	m_basicMeshes->DrawSphereMesh();

	//Inner cavity
	glm::vec3 innerScale = outerScale * 0.88f;
	glm::vec3 innerPos = bowlCenter + glm::vec3(0.0f, 0.18f, 0.0f);
	SetTransformations(innerScale, 0.0f, 0.0f, 0.0f, innerPos);

	SetShaderColor(0.05f, 0.05f, 0.05f, 1.0f);   // much darker inside
	SetShaderMaterial("stainless");
	m_basicMeshes->DrawSphereMesh();

	// Base ring
	glm::vec3 baseScale(1.2f, 0.15f, 1.2f);
	glm::vec3 basePos = bowlCenter + glm::vec3(0.0f, -(outerScale.y * 0.55f) + 0.08f, 0.0f);

	SetTransformations(baseScale, 0.0f, 0.0f, 0.0f, basePos);
	SetShaderColor(0.9f, 0.9f, 0.9f, 1.0f);
	SetShaderMaterial("stainless");
	m_basicMeshes->DrawCylinderMesh();
}



/***********************************************************
 *  LoadSceneTextures()
 *
 *  Loads textures used in the scene and binds them to texture
 ***********************************************************/
void SceneManager::LoadSceneTextures()
{
	//Milestone 4: Thermos textures
	bool bReturn = false;

	bReturn = CreateGLTexture("Utilities/textures/stainless.jpg", "stainless");
	bReturn = CreateGLTexture("Utilities/textures/stainless_red.jpg", "stainless_red");
	bReturn = CreateGLTexture("Utilities/textures/thermosbase.jpg", "thermosbase");
	bReturn = CreateGLTexture("Utilities/textures/rusticwood.jpg", "rusticwood");
	bReturn = CreateGLTexture("Utilities/textures/backdrop.jpg", "backdrop");
	bReturn = CreateGLTexture("Utilities/textures/book.jpg", "book");
	bReturn = CreateGLTexture("Utilities/textures/paper.jpg", "paper");
	bReturn = CreateGLTexture("Utilities/textures/gold-seamless-texture.jpg", "gold");

	if (!bReturn) std::cout << "One or more textures failed to load.\n";

	BindGLTextures();
}

/*Milestone 5: Added the DefineObjectMaterials() and SetupSceneLights() classes to configure materials.
*/

/***********************************************************
 *  DefineObjectMaterials()
 *  Configure materials used by the scene for Phong lighting.
 ***********************************************************/
void SceneManager::DefineObjectMaterials()
{
	m_objectMaterials.clear();		//Cleanliness check

	//Table, matte wood
	OBJECT_MATERIAL tableMat;
	tableMat.tag = "table";
	tableMat.ambientColor = glm::vec3(0.20f, 0.16f, 0.12f);
	tableMat.ambientStrength = 0.30f;
	tableMat.diffuseColor = glm::vec3(0.75f, 0.65f, 0.50f);
	tableMat.specularColor = glm::vec3(0.10f, 0.10f, 0.10f);
	tableMat.shininess = 8.0f;
	m_objectMaterials.push_back(tableMat);

	//Stainless, cap
	OBJECT_MATERIAL stainlessMat;
	stainlessMat.tag = "stainless";
	stainlessMat.ambientColor = glm::vec3(0.20f, 0.20f, 0.20f);
	stainlessMat.ambientStrength = 0.20f;
	stainlessMat.diffuseColor = glm::vec3(0.75f, 0.75f, 0.75f);
	stainlessMat.specularColor = glm::vec3(0.30f, 0.30f, 0.30f);
	stainlessMat.shininess = 30.0f;
	m_objectMaterials.push_back(stainlessMat);

	//Painted Plastic, body and thermosbase
	OBJECT_MATERIAL bodyMat;
	bodyMat.tag = "thermosbody";
	bodyMat.ambientColor = glm::vec3(0.18f, 0.18f, 0.18f);
	bodyMat.ambientStrength = 0.25f;
	bodyMat.diffuseColor = glm::vec3(0.85f, 0.85f, 0.85f);
	bodyMat.specularColor = glm::vec3(0.30f, 0.30f, 0.30f);
	bodyMat.shininess = 16.0f;
	m_objectMaterials.push_back(bodyMat);
}

/***********************************************************
 *  SetupSceneLights()
 *  Add and configure up to 4 light sources.
 ***********************************************************/
void SceneManager::SetupSceneLights()
{
	m_pShaderManager->setBoolValue(g_UseLightingName, true);		//Enable phong lighting


	//Light 0: neutral key light
	m_pShaderManager->setVec3Value("lightSources[0].position", 6.0f, 10.0f, 6.0f);
	m_pShaderManager->setVec3Value("lightSources[0].ambientColor", 0.12f, 0.12f, 0.12f);
	m_pShaderManager->setVec3Value("lightSources[0].diffuseColor", 0.85f, 0.85f, 0.85f);
	m_pShaderManager->setVec3Value("lightSources[0].specularColor", 0.35f, 0.35f, 0.35f);
	m_pShaderManager->setFloatValue("lightSources[0].focalStrength", 24.0f);
	m_pShaderManager->setFloatValue("lightSources[0].specularIntensity", 0.35f);

	//Light 1: colored fill light subtle magenta/purple
	m_pShaderManager->setVec3Value("lightSources[1].position", -6.0f, 4.0f, 2.0f);
	m_pShaderManager->setVec3Value("lightSources[1].ambientColor", 0.10f, 0.03f, 0.10f);
	m_pShaderManager->setVec3Value("lightSources[1].diffuseColor", 0.35f, 0.08f, 0.35f);
	m_pShaderManager->setVec3Value("lightSources[1].specularColor", 0.20f, 0.05f, 0.20f);
	m_pShaderManager->setFloatValue("lightSources[1].focalStrength", 18.0f);
	m_pShaderManager->setFloatValue("lightSources[1].specularIntensity", 0.25f);

	//Disable light 2 and 3 so that they are not causing errors.
	for (int i = 2; i < 4; ++i)
	{
		std::string idx = std::to_string(i);

		m_pShaderManager->setVec3Value(("lightSources[" + idx + "].position").c_str(), 0.0f, 0.0f, 0.0f);
		m_pShaderManager->setVec3Value(("lightSources[" + idx + "].ambientColor").c_str(), 0.0f, 0.0f, 0.0f);
		m_pShaderManager->setVec3Value(("lightSources[" + idx + "].diffuseColor").c_str(), 0.0f, 0.0f, 0.0f);
		m_pShaderManager->setVec3Value(("lightSources[" + idx + "].specularColor").c_str(), 0.0f, 0.0f, 0.0f);
		m_pShaderManager->setFloatValue(("lightSources[" + idx + "].focalStrength").c_str(), 0.0f);
		m_pShaderManager->setFloatValue(("lightSources[" + idx + "].specularIntensity").c_str(), 0.0f);
	}
}


/***********************************************************
 *  PrepareScene()
 *
 *  This method is used for preparing the 3D scene by loading
 *  the shapes, textures in memory to support the 3D scene
 *  rendering
 ***********************************************************/
void SceneManager::PrepareScene()
{
	// only one instance of a particular mesh needs to be
	// loaded in memory no matter how many times it is drawn
	// in the rendered 3D scene

	//Milestone 5: Added DefineObjectMaterial and SetupSceneLights.

	DefineObjectMaterials();
	SetupSceneLights();

	m_basicMeshes->LoadPlaneMesh();							//Prepared render meshes
	m_basicMeshes->LoadCylinderMesh();
	m_basicMeshes->LoadTaperedCylinderMesh();

	//Final Project: Added meshes for Boxes and Sphere

	m_basicMeshes->LoadBoxMesh();
	m_basicMeshes->LoadSphereMesh();

	//Milestone 4: load & bind textures for the scene
	LoadSceneTextures();
}

/***********************************************************
 *  RenderScene()
 *
 *  This method is used for rendering the 3D scene by
 *  transforming and drawing the basic 3D shapes
 ***********************************************************/
void SceneManager::RenderScene()
{
	RenderTable();
	RenderThermos();

	//Final Project: Added rendering for Book, Tin, Bowl

	RenderBook();
	RenderTin();
	RenderBowl();

}

