// Auto-generated. Do not edit!

// (in-package okao.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class face_info {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.face_count = null;
      this.id = null;
      this.x = null;
      this.y = null;
      this.size = null;
      this.conf = null;
      this.LR = null;
      this.UD = null;
      this.gazeLR = null;
      this.gazeUD = null;
    }
    else {
      if (initObj.hasOwnProperty('face_count')) {
        this.face_count = initObj.face_count
      }
      else {
        this.face_count = 0;
      }
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = [];
      }
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = [];
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = [];
      }
      if (initObj.hasOwnProperty('size')) {
        this.size = initObj.size
      }
      else {
        this.size = [];
      }
      if (initObj.hasOwnProperty('conf')) {
        this.conf = initObj.conf
      }
      else {
        this.conf = [];
      }
      if (initObj.hasOwnProperty('LR')) {
        this.LR = initObj.LR
      }
      else {
        this.LR = [];
      }
      if (initObj.hasOwnProperty('UD')) {
        this.UD = initObj.UD
      }
      else {
        this.UD = [];
      }
      if (initObj.hasOwnProperty('gazeLR')) {
        this.gazeLR = initObj.gazeLR
      }
      else {
        this.gazeLR = [];
      }
      if (initObj.hasOwnProperty('gazeUD')) {
        this.gazeUD = initObj.gazeUD
      }
      else {
        this.gazeUD = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type face_info
    // Serialize message field [face_count]
    bufferOffset = _serializer.int32(obj.face_count, buffer, bufferOffset);
    // Serialize message field [id]
    bufferOffset = _arraySerializer.int32(obj.id, buffer, bufferOffset, null);
    // Serialize message field [x]
    bufferOffset = _arraySerializer.int32(obj.x, buffer, bufferOffset, null);
    // Serialize message field [y]
    bufferOffset = _arraySerializer.int32(obj.y, buffer, bufferOffset, null);
    // Serialize message field [size]
    bufferOffset = _arraySerializer.int32(obj.size, buffer, bufferOffset, null);
    // Serialize message field [conf]
    bufferOffset = _arraySerializer.int32(obj.conf, buffer, bufferOffset, null);
    // Serialize message field [LR]
    bufferOffset = _arraySerializer.int32(obj.LR, buffer, bufferOffset, null);
    // Serialize message field [UD]
    bufferOffset = _arraySerializer.int32(obj.UD, buffer, bufferOffset, null);
    // Serialize message field [gazeLR]
    bufferOffset = _arraySerializer.int32(obj.gazeLR, buffer, bufferOffset, null);
    // Serialize message field [gazeUD]
    bufferOffset = _arraySerializer.int32(obj.gazeUD, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type face_info
    let len;
    let data = new face_info(null);
    // Deserialize message field [face_count]
    data.face_count = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [id]
    data.id = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [x]
    data.x = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [y]
    data.y = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [size]
    data.size = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [conf]
    data.conf = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [LR]
    data.LR = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [UD]
    data.UD = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [gazeLR]
    data.gazeLR = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [gazeUD]
    data.gazeUD = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.id.length;
    length += 4 * object.x.length;
    length += 4 * object.y.length;
    length += 4 * object.size.length;
    length += 4 * object.conf.length;
    length += 4 * object.LR.length;
    length += 4 * object.UD.length;
    length += 4 * object.gazeLR.length;
    length += 4 * object.gazeUD.length;
    return length + 40;
  }

  static datatype() {
    // Returns string type for a message object
    return 'okao/face_info';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '67bc21cec1ca544cbc5dca716a0b6dc0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 face_count
    int32[] id
    int32[] x
    int32[] y
    int32[] size
    int32[] conf
    int32[] LR
    int32[] UD
    int32[] gazeLR
    int32[] gazeUD
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new face_info(null);
    if (msg.face_count !== undefined) {
      resolved.face_count = msg.face_count;
    }
    else {
      resolved.face_count = 0
    }

    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = []
    }

    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = []
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = []
    }

    if (msg.size !== undefined) {
      resolved.size = msg.size;
    }
    else {
      resolved.size = []
    }

    if (msg.conf !== undefined) {
      resolved.conf = msg.conf;
    }
    else {
      resolved.conf = []
    }

    if (msg.LR !== undefined) {
      resolved.LR = msg.LR;
    }
    else {
      resolved.LR = []
    }

    if (msg.UD !== undefined) {
      resolved.UD = msg.UD;
    }
    else {
      resolved.UD = []
    }

    if (msg.gazeLR !== undefined) {
      resolved.gazeLR = msg.gazeLR;
    }
    else {
      resolved.gazeLR = []
    }

    if (msg.gazeUD !== undefined) {
      resolved.gazeUD = msg.gazeUD;
    }
    else {
      resolved.gazeUD = []
    }

    return resolved;
    }
};

module.exports = face_info;
