#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Float64.h"
#include "my_dynamixel_tutorial/servo_rad.h"
#include "my_dynamixel_tutorial/servo_speed.h"
#include <sstream>
#include <string>
#include <iostream>
#include <vector>
#include "my_dynamixel_tutorial/servo_service.h"
#include "dynamixel_msgs/JointState.h"

std_msgs::Float64 x;//dynamixel_managerへ送る速度情報か、角度情報をもつ
uint16_t id;        //サーボのidを一時的にもつ 使わなくても良い


ros::Publisher pub1;         //モータ1パブリッシャー
ros::Publisher pub2;         //モータ2パブリッシャー
ros::Publisher pub3;         //モータ3パブリッシャー
ros::Publisher pub4;         //モータ4パブリッシャー
ros::ServiceClient service;  //サービスクライアント


// サーボの角度を制御する役割
// 　servo_infoトピックを受け取った場合に、呼び出される。
// 　受け取ったメッセージに含まれるIDから、サーボを動作させるトピックを生成して
// 　動作させる角度を/dymamixel_managerへ配信する
void controlCallback(const my_dynamixel_tutorial::servo_rad msg)
{
  x.data = msg.rad;
  id = msg.id;
  ROS_INFO("received");

  std_msgs::String s;
  if(id==1){
  ROS_INFO("servo1:%lf",x.data);
  pub1.publish(x);                                                    //トピックを配信
  }
  else if(id==2){
  ROS_INFO("servo2:%lf",x.data);
  pub2.publish(x);                                                    //トピックを配信
  }
  else if(id==3){
  ROS_INFO("servo3:%lf",x.data);
  pub3.publish(x);                                                    //トピックを配信
  }
  else if(id==4){
  ROS_INFO("servo4:%lf",x.data);
  pub4.publish(x);                                                    //トピックを配信
  }
  else{ROS_INFO("invalid ID number");}
}
// サーボの速度を設定する役割
//　servo_set_speedトピックを受け取った場合に呼び出される
//　受け取ったメッセージに含まれるIDから、速度を変更するサービスを生成して
//　変更したい速度情報を/dynamixel_managerへサービス要求する。
void modifyCallback(const my_dynamixel_tutorial::servo_speed msg){
  x.data = msg.speed;
  ros::NodeHandle nh;
  std_msgs::String s;
  
  // std:: vector<std::string> str = {"/servo","_controller/set_speed"};
  std::stringstream topic_name; 
  topic_name << "/servo" << msg.id << "_controller/set_speed";                                      //サービス名を生成
  s.data = topic_name.str();
  service = nh.serviceClient<my_dynamixel_tutorial::servo_service>(s.data.c_str()); //サービスクライアントを生成
  ROS_INFO("%s",s.data.c_str());
  my_dynamixel_tutorial::servo_service srv;
  srv.request.speed = msg.speed;                                                 //サービスの速度変数にスピードを設定
  ROS_INFO("Id:%d, Speed:%lf",msg.id,x.data);  
  service.call(srv);
  if(service.call(srv)){                  //サービスを要求する
    ROS_INFO("Speed setting is Success");
  }else{
    ROS_ERROR("Failed");
  }
}



int main(int argc, char **argv)
{
  ros::init(argc,argv,"servo_manager");//他のノードからメッセージを受け取り、それを/dynamixe_managerの対応するトピックの形式にして配信、もしくは購買、サービス要求を行うノード
  ros::NodeHandle n;
  ros::Subscriber sub1 = n.subscribe("servo_info", 10, controlCallback);     //IDと角度情報を購買するトピック
  ros::Subscriber sub2 = n.subscribe("servo_set_speed", 10, modifyCallback); //IDとサーボ動作速度を購買するトピック
  pub1 = n.advertise<std_msgs::Float64>("/servo1_controller/command", 1000);        //モータ１のトピックを生成
  pub2 = n.advertise<std_msgs::Float64>("/servo2_controller/command", 1000);        //モータ2のトピックを生成
  pub3 = n.advertise<std_msgs::Float64>("/servo3_controller/command", 1000);        //モータ3のトピックを生成
  pub4 = n.advertise<std_msgs::Float64>("/servo4_controller/command", 1000);        //モータ4のトピックを生成

  ros::spin();
 return 0;
}


