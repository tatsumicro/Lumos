# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "okao: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iokao:/home/icd/catkin_ws/src/okao/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(okao_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/icd/catkin_ws/src/okao/msg/face_info.msg" NAME_WE)
add_custom_target(_okao_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "okao" "/home/icd/catkin_ws/src/okao/msg/face_info.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(okao
  "/home/icd/catkin_ws/src/okao/msg/face_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/okao
)

### Generating Services

### Generating Module File
_generate_module_cpp(okao
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/okao
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(okao_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(okao_generate_messages okao_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/icd/catkin_ws/src/okao/msg/face_info.msg" NAME_WE)
add_dependencies(okao_generate_messages_cpp _okao_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(okao_gencpp)
add_dependencies(okao_gencpp okao_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS okao_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(okao
  "/home/icd/catkin_ws/src/okao/msg/face_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/okao
)

### Generating Services

### Generating Module File
_generate_module_eus(okao
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/okao
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(okao_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(okao_generate_messages okao_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/icd/catkin_ws/src/okao/msg/face_info.msg" NAME_WE)
add_dependencies(okao_generate_messages_eus _okao_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(okao_geneus)
add_dependencies(okao_geneus okao_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS okao_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(okao
  "/home/icd/catkin_ws/src/okao/msg/face_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/okao
)

### Generating Services

### Generating Module File
_generate_module_lisp(okao
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/okao
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(okao_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(okao_generate_messages okao_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/icd/catkin_ws/src/okao/msg/face_info.msg" NAME_WE)
add_dependencies(okao_generate_messages_lisp _okao_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(okao_genlisp)
add_dependencies(okao_genlisp okao_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS okao_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(okao
  "/home/icd/catkin_ws/src/okao/msg/face_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/okao
)

### Generating Services

### Generating Module File
_generate_module_nodejs(okao
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/okao
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(okao_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(okao_generate_messages okao_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/icd/catkin_ws/src/okao/msg/face_info.msg" NAME_WE)
add_dependencies(okao_generate_messages_nodejs _okao_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(okao_gennodejs)
add_dependencies(okao_gennodejs okao_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS okao_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(okao
  "/home/icd/catkin_ws/src/okao/msg/face_info.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/okao
)

### Generating Services

### Generating Module File
_generate_module_py(okao
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/okao
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(okao_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(okao_generate_messages okao_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/icd/catkin_ws/src/okao/msg/face_info.msg" NAME_WE)
add_dependencies(okao_generate_messages_py _okao_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(okao_genpy)
add_dependencies(okao_genpy okao_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS okao_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/okao)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/okao
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(okao_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/okao)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/okao
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(okao_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/okao)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/okao
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(okao_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/okao)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/okao
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(okao_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/okao)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/okao\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/okao
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(okao_generate_messages_py std_msgs_generate_messages_py)
endif()
