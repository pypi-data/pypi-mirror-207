from pathlib import Path

from .SHHSAnnotationLoader import SHHSAnnotationLoader
from pyPhasesRecordloader.recordLoaders.EDFRecordLoader import EDFRecordLoader


class RecordLoaderSHHS(EDFRecordLoader):
    def __init__(
        self,
        filePath,
        targetSignals,
        targetSignalTypes=[],
        optionalSignals=[],
        combineChannels=[],
    ) -> None:
        super().__init__(
            filePath,
            targetSignals,
            targetSignalTypes=targetSignalTypes,
            optionalSignals=optionalSignals,
            combineChannels=combineChannels,
        )

        self.exportsEventArray = True

    def getFileBasePath(self, recrdId):
        return self.filePath

    def getFilePathSignal(self, recordId):
        
        return f"{self.getFileBasePath(recordId)}/polysomnography/edfs/shhs1/{recordId}.edf"

    def getFilePathAnnotation(self, recordId):
        return f"{self.getFileBasePath(recordId)}/polysomnography/annotations-events-nsrr/shhs1/{recordId}-nsrr.xml"

    def existAnnotation(self, recordId):
        return Path(self.getFilePathAnnotation(recordId)).exists()

    def exist(self, recordId):
        return Path(self.getFilePathAnnotation(recordId)).exists() & Path(self.getFilePathSignal(recordId)).exists()

    def loadAnnotation(self, recordId, fileName, valueMap=None):
        filePath = self.getFilePathAnnotation(recordId)
        annotationLoader = SHHSAnnotationLoader.load(filePath, valueMap, self.annotationFrequency)

        return annotationLoader.events

    def getEventList(self, recordName, targetFrequency=1):
        metaXML = self.getFilePathAnnotation(recordName)
        xmlLoader = SHHSAnnotationLoader()

        eventArray = xmlLoader.loadAnnotation(metaXML)
        self.lightOff = xmlLoader.lightOff
        self.lightOn = xmlLoader.lightOn

        if targetFrequency != 1:
            eventArray = self.updateFrequencyForEventList(eventArray, targetFrequency)

        return eventArray

    # def getMetaData(self, recordName) -> Record:

    #     self.frequency = 0

    #     edfFile = self.getFilePathSignal(recordName)

    #     record = Record()
    #     self.fillRecordFromEdf(record, edfFile)

    #     return record
