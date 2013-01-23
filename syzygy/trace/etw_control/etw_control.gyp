# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'targets': [
    {
      'target_name': 'etw_control_lib',
      'type': 'static_library',
      'sources': [
        'call_trace_control.cc',
        'call_trace_control.h',
      ],
      'dependencies': [
        '<(src)/syzygy/trace/rpc/rpc.gyp:rpc_common_lib',
      ],
    },
    {
      'target_name': 'call_trace_control',
      'type': 'executable',
      'sources': [
        'call_trace_control_main.cc',
        'call_trace_control.rc',
      ],
      'dependencies': [
        'etw_control_lib',
        '<(src)/base/base.gyp:base',
        '<(src)/sawbuck/common/common.gyp:common',
        '<(src)/syzygy/trace/rpc/rpc.gyp:rpc_common_lib',
      ],
    },
  ],
}
