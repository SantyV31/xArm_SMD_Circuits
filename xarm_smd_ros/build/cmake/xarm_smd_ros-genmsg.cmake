# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "xarm_smd_ros: 3 messages, 0 services")

set(MSG_I_FLAGS "-Ixarm_smd_ros:/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(xarm_smd_ros_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg" NAME_WE)
add_custom_target(_xarm_smd_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xarm_smd_ros" "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg" ""
)

get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg" NAME_WE)
add_custom_target(_xarm_smd_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xarm_smd_ros" "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg" "xarm_smd_ros/Componente"
)

get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg" NAME_WE)
add_custom_target(_xarm_smd_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "xarm_smd_ros" "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xarm_smd_ros
)
_generate_msg_cpp(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg"
  "${MSG_I_FLAGS}"
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xarm_smd_ros
)
_generate_msg_cpp(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xarm_smd_ros
)

### Generating Services

### Generating Module File
_generate_module_cpp(xarm_smd_ros
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xarm_smd_ros
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(xarm_smd_ros_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(xarm_smd_ros_generate_messages xarm_smd_ros_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_cpp _xarm_smd_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_cpp _xarm_smd_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_cpp _xarm_smd_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xarm_smd_ros_gencpp)
add_dependencies(xarm_smd_ros_gencpp xarm_smd_ros_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xarm_smd_ros_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xarm_smd_ros
)
_generate_msg_eus(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg"
  "${MSG_I_FLAGS}"
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xarm_smd_ros
)
_generate_msg_eus(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xarm_smd_ros
)

### Generating Services

### Generating Module File
_generate_module_eus(xarm_smd_ros
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xarm_smd_ros
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(xarm_smd_ros_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(xarm_smd_ros_generate_messages xarm_smd_ros_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_eus _xarm_smd_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_eus _xarm_smd_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_eus _xarm_smd_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xarm_smd_ros_geneus)
add_dependencies(xarm_smd_ros_geneus xarm_smd_ros_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xarm_smd_ros_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xarm_smd_ros
)
_generate_msg_lisp(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg"
  "${MSG_I_FLAGS}"
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xarm_smd_ros
)
_generate_msg_lisp(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xarm_smd_ros
)

### Generating Services

### Generating Module File
_generate_module_lisp(xarm_smd_ros
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xarm_smd_ros
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(xarm_smd_ros_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(xarm_smd_ros_generate_messages xarm_smd_ros_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_lisp _xarm_smd_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_lisp _xarm_smd_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_lisp _xarm_smd_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xarm_smd_ros_genlisp)
add_dependencies(xarm_smd_ros_genlisp xarm_smd_ros_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xarm_smd_ros_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xarm_smd_ros
)
_generate_msg_nodejs(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg"
  "${MSG_I_FLAGS}"
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xarm_smd_ros
)
_generate_msg_nodejs(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xarm_smd_ros
)

### Generating Services

### Generating Module File
_generate_module_nodejs(xarm_smd_ros
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xarm_smd_ros
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(xarm_smd_ros_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(xarm_smd_ros_generate_messages xarm_smd_ros_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_nodejs _xarm_smd_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_nodejs _xarm_smd_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_nodejs _xarm_smd_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xarm_smd_ros_gennodejs)
add_dependencies(xarm_smd_ros_gennodejs xarm_smd_ros_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xarm_smd_ros_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xarm_smd_ros
)
_generate_msg_py(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg"
  "${MSG_I_FLAGS}"
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xarm_smd_ros
)
_generate_msg_py(xarm_smd_ros
  "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xarm_smd_ros
)

### Generating Services

### Generating Module File
_generate_module_py(xarm_smd_ros
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xarm_smd_ros
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(xarm_smd_ros_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(xarm_smd_ros_generate_messages xarm_smd_ros_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Componente.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_py _xarm_smd_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/ListaComponentes.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_py _xarm_smd_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/andy/tesis_xarm_ws/src/xarm_smd_ros/msg/Posicion.msg" NAME_WE)
add_dependencies(xarm_smd_ros_generate_messages_py _xarm_smd_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(xarm_smd_ros_genpy)
add_dependencies(xarm_smd_ros_genpy xarm_smd_ros_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS xarm_smd_ros_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xarm_smd_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/xarm_smd_ros
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(xarm_smd_ros_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xarm_smd_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/xarm_smd_ros
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(xarm_smd_ros_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xarm_smd_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/xarm_smd_ros
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(xarm_smd_ros_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xarm_smd_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/xarm_smd_ros
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(xarm_smd_ros_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xarm_smd_ros)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xarm_smd_ros\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/xarm_smd_ros
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(xarm_smd_ros_generate_messages_py std_msgs_generate_messages_py)
endif()
