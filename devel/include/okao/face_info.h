// Generated by gencpp from file okao/face_info.msg
// DO NOT EDIT!


#ifndef OKAO_MESSAGE_FACE_INFO_H
#define OKAO_MESSAGE_FACE_INFO_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace okao
{
template <class ContainerAllocator>
struct face_info_
{
  typedef face_info_<ContainerAllocator> Type;

  face_info_()
    : face_count(0)
    , id()
    , x()
    , y()
    , size()
    , conf()
    , LR()
    , UD()
    , gazeLR()
    , gazeUD()  {
    }
  face_info_(const ContainerAllocator& _alloc)
    : face_count(0)
    , id(_alloc)
    , x(_alloc)
    , y(_alloc)
    , size(_alloc)
    , conf(_alloc)
    , LR(_alloc)
    , UD(_alloc)
    , gazeLR(_alloc)
    , gazeUD(_alloc)  {
  (void)_alloc;
    }



   typedef int32_t _face_count_type;
  _face_count_type face_count;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _id_type;
  _id_type id;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _x_type;
  _x_type x;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _y_type;
  _y_type y;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _size_type;
  _size_type size;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _conf_type;
  _conf_type conf;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _LR_type;
  _LR_type LR;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _UD_type;
  _UD_type UD;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _gazeLR_type;
  _gazeLR_type gazeLR;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _gazeUD_type;
  _gazeUD_type gazeUD;





  typedef boost::shared_ptr< ::okao::face_info_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::okao::face_info_<ContainerAllocator> const> ConstPtr;

}; // struct face_info_

typedef ::okao::face_info_<std::allocator<void> > face_info;

typedef boost::shared_ptr< ::okao::face_info > face_infoPtr;
typedef boost::shared_ptr< ::okao::face_info const> face_infoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::okao::face_info_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::okao::face_info_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace okao

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'okao': ['/home/icd/catkin_ws/src/okao/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::okao::face_info_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::okao::face_info_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::okao::face_info_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::okao::face_info_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::okao::face_info_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::okao::face_info_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::okao::face_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "67bc21cec1ca544cbc5dca716a0b6dc0";
  }

  static const char* value(const ::okao::face_info_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x67bc21cec1ca544cULL;
  static const uint64_t static_value2 = 0xbc5dca716a0b6dc0ULL;
};

template<class ContainerAllocator>
struct DataType< ::okao::face_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "okao/face_info";
  }

  static const char* value(const ::okao::face_info_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::okao::face_info_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 face_count\n\
int32[] id\n\
int32[] x\n\
int32[] y\n\
int32[] size\n\
int32[] conf\n\
int32[] LR\n\
int32[] UD\n\
int32[] gazeLR\n\
int32[] gazeUD\n\
";
  }

  static const char* value(const ::okao::face_info_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::okao::face_info_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.face_count);
      stream.next(m.id);
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.size);
      stream.next(m.conf);
      stream.next(m.LR);
      stream.next(m.UD);
      stream.next(m.gazeLR);
      stream.next(m.gazeUD);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct face_info_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::okao::face_info_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::okao::face_info_<ContainerAllocator>& v)
  {
    s << indent << "face_count: ";
    Printer<int32_t>::stream(s, indent + "  ", v.face_count);
    s << indent << "id[]" << std::endl;
    for (size_t i = 0; i < v.id.size(); ++i)
    {
      s << indent << "  id[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.id[i]);
    }
    s << indent << "x[]" << std::endl;
    for (size_t i = 0; i < v.x.size(); ++i)
    {
      s << indent << "  x[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.x[i]);
    }
    s << indent << "y[]" << std::endl;
    for (size_t i = 0; i < v.y.size(); ++i)
    {
      s << indent << "  y[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.y[i]);
    }
    s << indent << "size[]" << std::endl;
    for (size_t i = 0; i < v.size.size(); ++i)
    {
      s << indent << "  size[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.size[i]);
    }
    s << indent << "conf[]" << std::endl;
    for (size_t i = 0; i < v.conf.size(); ++i)
    {
      s << indent << "  conf[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.conf[i]);
    }
    s << indent << "LR[]" << std::endl;
    for (size_t i = 0; i < v.LR.size(); ++i)
    {
      s << indent << "  LR[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.LR[i]);
    }
    s << indent << "UD[]" << std::endl;
    for (size_t i = 0; i < v.UD.size(); ++i)
    {
      s << indent << "  UD[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.UD[i]);
    }
    s << indent << "gazeLR[]" << std::endl;
    for (size_t i = 0; i < v.gazeLR.size(); ++i)
    {
      s << indent << "  gazeLR[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.gazeLR[i]);
    }
    s << indent << "gazeUD[]" << std::endl;
    for (size_t i = 0; i < v.gazeUD.size(); ++i)
    {
      s << indent << "  gazeUD[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.gazeUD[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // OKAO_MESSAGE_FACE_INFO_H