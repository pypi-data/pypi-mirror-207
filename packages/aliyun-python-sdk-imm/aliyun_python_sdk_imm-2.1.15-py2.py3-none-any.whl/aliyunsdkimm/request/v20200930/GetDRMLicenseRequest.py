# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkimm.endpoint import endpoint_data

class GetDRMLicenseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'GetDRMLicense','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProtectionSystem(self): # String
		return self.get_query_params().get('ProtectionSystem')

	def set_ProtectionSystem(self, ProtectionSystem):  # String
		self.add_query_param('ProtectionSystem', ProtectionSystem)
	def get_NotifyEndpoint(self): # String
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self, NotifyEndpoint):  # String
		self.add_query_param('NotifyEndpoint', NotifyEndpoint)
	def get_ProjectName(self): # String
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_query_param('ProjectName', ProjectName)
	def get_NotifyTopicName(self): # String
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self, NotifyTopicName):  # String
		self.add_query_param('NotifyTopicName', NotifyTopicName)
	def get_KeyId(self): # String
		return self.get_query_params().get('KeyId')

	def set_KeyId(self, KeyId):  # String
		self.add_query_param('KeyId', KeyId)
