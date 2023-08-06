from distillation.utils import *
from fastai.vision.all import *
import fastai
import torchvision.models as models
import shutil
import os


def plainDistillation(baseModel, targetModel, path, pathUnlabelled, outputPath, bs=32, size=224, confidence=0.8):
    if not testNameModel(baseModel):
        print("The base model selected is not valid")
    elif not testNameModel(targetModel):
        print("The target model selected is not valid")
    elif not testPath(path):
        print("The path is invalid or has an invalid structure")
    else:
        # Load images
        dls = ImageDataLoaders.from_folder(path, batch_tfms=aug_transforms(), item_tfms=Resize(size), bs=bs)

        # Load base model
        bModel=getModel(baseModel,dls.c)

        # Create base learner
        save = SaveModelCallback(monitor='accuracy', fname='model-'+baseModel)
        early = EarlyStoppingCallback(monitor='accuracy', patience=8)
        learn = Learner(dls, bModel, metrics=[accuracy], cbs=[early, save])

        # Train base learner
        print("Start of base model training")
        train_learner(learn, 50, freeze_epochs=2)
        # learn.fine_tune(50, freeze_epochs=2)
        learn.save(baseModel)
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)
        shutil.copy(path+os.sep+'models'+os.sep+baseModel+'.pth',outputPath+os.sep+'base_'+baseModel+'.pth')

        # supervised method
        print("Start of annotation")
        plainSupervised(path,pathUnlabelled,learn,confidence)
        print("End of annotation")

        # Load new images
        dls2 = ImageDataLoaders.from_folder(path+'_tmp', batch_tfms=aug_transforms(), item_tfms=Resize(size), bs=bs)

        # Load base model
        tModel = getModel(targetModel, dls2.c)

        # Create base learner
        save2 = SaveModelCallback(monitor='accuracy', fname='model-' + targetModel)
        early2 = EarlyStoppingCallback(monitor='accuracy', patience=8)
        learn2 = Learner(dls2, tModel, metrics=[accuracy], cbs=[early2, save2])


        # Train base learner
        print("Start of target model training")
        train_learner(learn2, 50, freeze_epochs=2)
        # learn2.fine_tune(50, freeze_epochs=2)
        learn2.save(targetModel)
        shutil.copy(path+'_tmp'+os.sep+'models' + os.sep + targetModel + '.pth', outputPath+os.sep+'target_'+targetModel+'.pth')
        shutil.rmtree(path+'_tmp')



def dataDistillation(baseModel, targetModel, transforms, path, pathUnlabelled, outputPath, bs=32, size=224, confidence=0.8):
    if not testNameModel(baseModel):
        print("The base model selected is not valid")
    elif not testNameModel(targetModel):
        print("The target model selected is not valid")
    elif not testPath(path):
        print("The path is invalid or has an invalid structure")
    elif not testTransforms(transforms):
        print("There are invalid transforms")
    else:
        # Load images
        dls = ImageDataLoaders.from_folder(path, batch_tfms=aug_transforms(), item_tfms=Resize(size), bs=bs)

        # Load base model
        bModel = getModel(baseModel, dls.c)

        # Create base learner
        save = SaveModelCallback(monitor='accuracy', fname='model-' + baseModel)
        early = EarlyStoppingCallback(monitor='accuracy', patience=8)
        learn = Learner(dls, bModel, splitter=default_split, metrics=[accuracy], cbs=[early, save])

        # Train base learner
        print("Start of base model training")
        train_learner(learn, 50, freeze_epochs=2)
        # learn.fine_tune(50, freeze_epochs=2)
        learn.save(baseModel)
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)
        shutil.copy(path+os.sep+'models'+os.sep+baseModel+'.pth',outputPath+os.sep+'base_'+baseModel+'.pth')

        # supervised method
        print("Start of annotation")
        omniData(path, pathUnlabelled, learn, transforms,confidence)
        print("End of annotation")

        # Load new images
        dls2 = ImageDataLoaders.from_folder(path + '_tmp', batch_tfms=aug_transforms(), item_tfms=Resize(size), bs=bs)

        # Load base model
        tModel = getModel(targetModel, dls2.c)

        # Create base learner
        save2 = SaveModelCallback(monitor='accuracy', fname='model-' + targetModel)
        early2 = EarlyStoppingCallback(monitor='accuracy', patience=8)
        learn2 = Learner(dls2, tModel, splitter=default_split, metrics=[accuracy], cbs=[early2, save2])

        # Train base learner
        print("Start of target model training")
        train_learner(learn2, 50, freeze_epochs=2)
        # learn2.fine_tune(50, freeze_epochs=2)
        learn2.save(targetModel)
        shutil.copy(path + '_tmp' + os.sep + 'models' + os.sep + targetModel + '.pth',
                    outputPath + os.sep + 'target_' + targetModel + '.pth')
        shutil.rmtree(path + '_tmp')


def modelDistillation(baseModels, targetModel, path, pathUnlabelled, outputPath, bs=32, size=224, confidence=0.8):
    for baseModel in baseModels:
        if not testNameModel(baseModel):
            print("The base model selected is not valid")
            return
    if not testNameModel(targetModel):
        print("The target model selected is not valid")
    elif not testPath(path):
        print("The path is invalid or has an invalid structure")
    else:
        # Load images
        dls = ImageDataLoaders.from_folder(path, batch_tfms=aug_transforms(), item_tfms=Resize(size), bs=bs)

        # Load base model
        learners=[]
        print("Start of base models training")
        for baseModel in baseModels:
            bModel = getModel(baseModel, dls.c)

            # Create base learner
            save = SaveModelCallback(monitor='accuracy', fname='model-' + baseModel)
            early = EarlyStoppingCallback(monitor='accuracy', patience=8)

            learn = Learner(dls, bModel, splitter=default_split, metrics=[accuracy], cbs=[early, save])

            # Train base learner
            train_learner(learn, 50, freeze_epochs=2)
            # learn.fine_tune(50, freeze_epochs=2)
            learn.save(baseModel)
            if not os.path.exists(outputPath):
                os.makedirs(outputPath)
            shutil.copy(path + os.sep + 'models' + os.sep + baseModel + '.pth',
                        outputPath + os.sep + 'base_' + baseModel + '.pth')
            learners.append(learn)


        # supervised method
        print("Start of annotation")
        omniModel(path, pathUnlabelled, learners, confidence)
        print("End of annotation")

        # Load new images
        dls2 = ImageDataLoaders.from_folder(path + '_tmp', batch_tfms=aug_transforms(), item_tfms=Resize(size), bs=bs)

        # Load base model
        tModel = getModel(targetModel, dls2.c)

        # Create base learner
        save2 = SaveModelCallback(monitor='accuracy', fname='model-' + targetModel)
        early2 = EarlyStoppingCallback(monitor='accuracy', patience=8)
        learn2 = Learner(dls2, tModel, splitter=default_split, metrics=[accuracy], cbs=[early2, save2])

        # Train base learner
        print("Start of target model training")
        train_learner(learn2, 50, freeze_epochs=2)
        # learn2.fine_tune(50, freeze_epochs=2)
        learn2.save(targetModel)
        shutil.copy(path + '_tmp' + os.sep + 'models' + os.sep + targetModel + '.pth',
                    outputPath + os.sep + 'target_' + targetModel + '.pth')
        shutil.rmtree(path + '_tmp')


def modelDataDistillation(baseModels, targetModel, transforms, path, pathUnlabelled, outputPath, bs=32, size=224, confidence=0.8):
    for baseModel in baseModels:
        if not testNameModel(baseModel):
            print("The base model selected is not valid")
            return
    if not testNameModel(targetModel):
        print("The target model selected is not valid")
    elif not testPath(path):
        print("The path is invalid or has an invalid structure")
    elif not testTransforms(transforms):
        print("There are invalid transforms")
    else:
        # Load images
        learners=[]
        print("Start of base models training")
        for baseModel in baseModels:
            dls = ImageDataLoaders.from_folder(path, batch_tfms=aug_transforms(), item_tfms=Resize(size), bs=bs)

            # Load base model
            bModel = getModel(baseModel, dls.c)

            # Create base learner
            save = SaveModelCallback(monitor='accuracy', fname='model-' + baseModel)
            early = EarlyStoppingCallback(monitor='accuracy', patience=8)
            learn = Learner(dls, bModel, splitter=default_split, metrics=[accuracy], cbs=[early, save])

            # Train base learner
            train_learner(learn, 50, freeze_epochs=2)
            # learn.fine_tune(50, freeze_epochs=2)
            learn.save(baseModel)
            if not os.path.exists(outputPath):
                os.makedirs(outputPath)
            shutil.copy(path + os.sep + 'models' + os.sep + baseModel + '.pth',
                        outputPath + os.sep + 'base_' + baseModel + '.pth')
            learners.append(learn)

        # supervised method
        print("Start of annotation")
        omniModelData(path, pathUnlabelled, learners, transforms,confidence)
        print("End of annotation")

        # Load new images
        dls2 = ImageDataLoaders.from_folder(path + '_tmp', batch_tfms=aug_transforms(), item_tfms=Resize(size), bs=bs)

        # Load base model
        tModel = getModel(targetModel, dls2.c)

        # Create base learner
        save2 = SaveModelCallback(monitor='accuracy', fname='model-' + targetModel)
        early2 = EarlyStoppingCallback(monitor='accuracy', patience=8)
        learn2 = Learner(dls2, tModel, splitter=default_split, metrics=[accuracy], cbs=[early2, save2])

        # Train base learner
        print("Start of target model training")
        train_learner(learn2, 50, freeze_epochs=2)
        # learn2.fine_tune(50, freeze_epochs=2)
        learn2.save(targetModel)
        shutil.copy(path + '_tmp' + os.sep + 'models' + os.sep + targetModel + '.pth',
                    outputPath + os.sep + 'target_' + targetModel + '.pth')
        shutil.rmtree(path + '_tmp')

def simpleTraining(baseModel, path, outputPath, bs=32, size=224):
    if not testNameModel(baseModel):
        print("The base model selected is not valid")
    elif not testPath(path):
        print("The path is invalid or has an invalid structure")
    else:
        # Load images
        dls = ImageDataLoaders.from_folder(path, batch_tfms=aug_transforms(), item_tfms=Resize(size), bs=bs)

        # Load base model
        bModel=getModel(baseModel,dls.c)

        # Create base learner
        save = SaveModelCallback(monitor='accuracy', fname='model-'+baseModel)
        early = EarlyStoppingCallback(monitor='accuracy', patience=8)
        learn = Learner(dls, bModel, metrics=[accuracy], cbs=[early, save])

        # Train base learner
        print("Start of model training")
        train_learner(learn, 50, freeze_epochs=2)
        # learn.fine_tune(50, freeze_epochs=2)
        learn.save(baseModel)
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)
        shutil.copy(path+os.sep+'models'+os.sep+baseModel+'.pth',outputPath+os.sep+'target_'+baseModel+'.pth')
