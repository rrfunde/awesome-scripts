#!/bin/bash

e=$(networksetup -getwebproxy wi-fi | grep "No")

if [ -n "$e" ]; then
  sudo networksetup -setsecurewebproxy "Wi-Fi" put_your_proxy_server_address put_port_number
  sudo networksetup -setwebproxy "Wi-Fi" put_your_proxy_server_address put_port_number
  echo "proxy set"
else
  sudo networksetup -setwebproxystate "Wi-Fi" off
  sudo networksetup -setsecurewebproxystate "Wi-Fi" off
  echo "proxy unset"
fi
