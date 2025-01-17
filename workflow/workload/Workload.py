import numpy as np

class Workload():
	def __init__(self):
		self.workflow_id = 0
		self.creation_id = 0
		self.createdContainers = [] # 已创建容器
		self.deployedContainers = [] # 已部署容器

	def getUndeployedContainers(self):
		undeployed = []
		for i,deployed in enumerate(self.deployedContainers):
			if not deployed:
				undeployed.append(self.createdContainers[i])
		return undeployed

	def updateDeployedContainers(self, creationIDs):
		for cid in creationIDs:
			assert not self.deployedContainers[cid]
			self.deployedContainers[cid] = True
