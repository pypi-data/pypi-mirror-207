"""
Base class for intensity measuremt on the reference images.
"""

import tifffile
import napari
from scipy.ndimage import median_filter
from skimage import measure
import numpy as np
import pandas as pd

from stardist.models import StarDist2D
from csbdeep.utils import normalize
# creates a pretrained model
model = StarDist2D.from_pretrained('2D_versatile_fluo')

class ReferenceImage:

    # class attribute to store info abound imaging,smoothing, segmentation-
    # settings.
    metadata = {}
    
    # this class attribute store all the instances created using this class
    all_fovs = []
    def __init__(
        self,
        root_path:str='',
        file_path:str='',
        field_of_view:str='',
        probe1_name:str=None,
        probe2_name:str=None,
        transmitted_name:str=None,
        imaging_setup:dict={}):
        """ReferenceImage class load tiff images, do meadian
        filtering and stardist2D segmentation and computes area
        and mean intensity per pixel.

        Parameters
        ----------
        root_path, file_path : str, optional
            Full path to tiff images are separated in `root_path`
            and `file_path` for convention. Therefore, full path 
            to a image file = `root_path`+`file_path`,by default ''
        field_of_view : str, optional
            Prefix of the file name. eg. fv1, by default None
        probe1_name,probe2_name,transmitted_name : str, optional
            Name of probes to register, by default None.
            If no probe_name is provided, no image will be loaded.
        imaging_setup : dict, optional
            A key of metadata attribute of ReferenceImage class, 
            by default empty dict. This variable is created to 
            store general information of imaging setting. E.g.
            imaging_setup = {
                        'laser': [647, 488],
                        'internal_power_percetage':[60,60],
                        'external_power_percetage':[0.1,0.1],
                        'camera_exposure_ms':[100,100],
                        }
        """
        self.root_path = root_path
        self.file_path = file_path
        self.field_of_view = field_of_view
        self.probe1_name = probe1_name
        self.probe2_name = probe2_name
        self.transmitted_name = transmitted_name
        self.metadata['imaging_setup'] = imaging_setup
    
        # load the images 
        self.image = {}

        path_prefix = self.root_path+self.file_path+self.field_of_view+' '

        if self.transmitted_name is not None:
            self.image[f"{self.transmitted_name}"] = tifffile.imread(
                path_prefix+self.transmitted_name+'.tif')
        
        if self.probe1_name is not None:
            self.image[f"{self.probe1_name}"] = tifffile.imread(
                path_prefix+self.probe1_name+'.tif')
        
        if self.probe2_name is not None:
            self.image[f"{self.probe2_name}"] = tifffile.imread(
                path_prefix+self.probe2_name+'.tif')
        
        print(f"ReferenceImage created with: {list(self.image.keys())}")
        # 
        ReferenceImage.all_fovs.append(self)
    
    def show_image_names(self):
        print(list(self.image.keys()))
        return 
        
    def view_on_napari(self,pixel_length_um=0.1, return_viewer:bool=False)->napari.Viewer:
        """Displays the availlable images in napari viewer.

        If no image is found, no viewer object will be returned.

        Parameters
        ----------
        return_viewer : bool, optional
            If True, returns napari.Viewer object, by default False

        Returns
        -------
        napari.Viewer
            Viewer containing all the available images.
        """
        if len(self.image) == 0:
            print(f"Image not found!!")
            return
        else:
            viewer = napari.Viewer()
            for image_name,image in self.image.items():
                if 'label' in image_name:
                    # viewer.add_labels(image, name=image_name))
                    viewer.add_labels(image, name=image_name,scale=(pixel_length_um,pixel_length_um))
                else:
                    viewer.add_image(image, name=image_name,scale=(pixel_length_um,pixel_length_um))
            viewer.scale_bar.visible = True
            viewer.scale_bar.unit="um"       
            if return_viewer:
                return viewer
            else:
                return
    

    def smoothing(self,image_name:str=None,sigma:int=8,return_image:bool=False):
        """Performs median filtering using scipy library.

        Parameters
        ----------
        image_name : str, optional
            Either `probe1_name` or `probe2_name`, by default `probe1_name`
        sigma : int, optional
            The size of smoothing kernel in pixel, by default 8
        return_image : bool, optional
            If Ture, return the smoothed image, by default False

        Returns
        -------
        (None or np.ndarry)
            numpy.ndarray if `return_image` is set True.
        """   

        # assert if the valid image_name is given
        # list(self.image.keys())     
        if image_name is None:
            image_name = self.probe1_name
        else:
            assert image_name in list(self.image.keys()),\
                  f"No valid image_name is given.\
                    Available image_names:{ReferenceImage.show_image_names(self)}"
        
        self.image[f"MedianFiltered_{sigma}px"] = median_filter(
            self.image[image_name], size=sigma)
            
        self.metadata['smoothing'] = {'image_name':image_name,'sigma':sigma}
        if return_image:
            return self.image[f"MedianFiltered_{sigma}px"]
        else:
            return

    def run_segmentaion2d(
            self,
            image_name:str=None,
            prob_thresh:float=0.5,
            nms_threhold:float=0.01,
            scale:float=0.2,
            return_results:bool=False,
            verbose:bool=False)->tuple:
        """Performs stardist 2D segmentation and removes boundary
        nucleus labes.

        The segmentation is done with stardist2D using the 
        model '2D_versatile_fluo'. Add `image['labels']`, `polys`,
        and `contours` properties in the instance inplace.

        Parameters
        ----------
        image_name : str, optional
            Name of image to segment, by default None.
            None value results to choose the image_name to
            be the median filtered (smoothed) image.
        prob_thresh : float, optional
            Probability threshold value, by default 0.5.
            Higher the `prob_thresh` value leads to removal
            of less confident images.
        nms_threhold : float, optional
            Non-maximum supression threshold is the value, 
            allowed to overlap between two nuclei.by default 0.01
            If the overlapped area of the nucleus is greater than
            this value, smaller nuclei is 
        scale : float, optional
            Scaleing factor for the image prior the segmentaion, 
            by default 0.2. scale = 1 means no rescaling.
        return_results : bool, optional
            If true through results, by default False
        verbose : bool, optional
            Whether to display progressbar, dy default False

        Returns
        -------
        tuple
            If `return_result` is set True, tuple of label image
            -containing nuclear mask, starddist polys - dict containing
            32 boundary coords and its center points for each nucleus,
            and contour- list of nuclear boundary points is returned.
        """
        # get the valid image name for segmentaion
        if image_name is None:
            image_name = f"MedianFiltered_{self.metadata['smoothing']['sigma']}px"
        else:
            assert image_name in list(self.image.keys()),\
                  f"No valid image_name is given.\
                    Available image_names:{ReferenceImage.show_image_names(self)}"

        # main segmentation 
        self.image['labels'], self.polys = model.predict_instances(
            normalize(self.image[image_name]),
            prob_thresh=prob_thresh,  # adjust thie parameter
            nms_thresh=nms_threhold, 
            scale=scale, 
            verbose=verbose,
            axes='YX',
            n_tiles=None,
            overlap_label=None, # if not None, label the regions where polygons overlap with that value
            )
        
        # find contours
        self.contours = ReferenceImage.find_contours(self.image['labels'])

        # store used paramters for segmentation in metadata
        self.metadata['segmentation'] = {
            'prob_thresh':prob_thresh, 
            'nms_threhold':nms_threhold,
            'scale':scale }

        if return_results:
            return self.image['labels'], self.polys, self.contours
        else:
            return
    
    @staticmethod
    def find_contours(label_image:np.ndarray)->list:
        """Find the contours from label image.

        Parameters
        ----------
        label_image : numpy.ndarray
            The label image.

        Returns
        -------
        list
            Each element of the list contains two-dimensaional
            points denoting a contour.
        """
        # 
        contours = []
        for label in np.unique(label_image):
            if label == 0:
                continue
            mask = label_image == label
            contours.append(measure.find_contours(mask, 0.5)[0])
        return contours
    
    def filter_by_boundary_n_area(self,
                              a_pixel_area:float = 0.01,
                              area_threshold:list=[80,200]):
        """Removed the nuclear labels that are at the boundary 
        of the field of view and are not within the `area_threshold`.

        This method adds `image['boundary_filtered_labels']`,  
        `image['area_filtered_labels']` the  following attributes in
        the self object.
        `n_contours`: Number of nucleus detected
        `is_closed` : Boolean mask whether each detected nucleus is 
            at the boundary of field of view or not.
        `closedcontours`: Contains index of labels that are not at
            the boundary.
        `n_closedcontours`: Number of nuclear mask that does not lie
            at the boundary.
        `n_true_nucleus`: Number of nucleus those are not in the boundary
            and pass the area_threshold.

        Parameters
        ----------
        a_pixel_area   : float, optional
            Area of a unit pixel in um^2. Default to 0.01 um^2.
        area_threshold: list, optional
            List containing the minimum and maximum area that each nucleus 
            can have. Default area_min = 80 um^2 and area_max = 200 um^2

        Returns
        -------
        None
            Save the results inplace
        """
         # count number of contours i.e. original cell detected by stardist
        self.n_contours = len(self.contours)
        is_closed = np.full((self.n_contours,),fill_value=False)
        for i,contour in enumerate(self.contours):
            is_closed[i] = np.allclose(contour[0], contour[-1])

        # store boolean array whether each contour is complete or not
        self.is_closed = is_closed
        # store index of closed contours
        self.closedcontours = np.where(self.is_closed==True)[0]
        # store number of closed contours
        self.n_closedcontours = len(self.closedcontours)

        # boundary filtered nucleus or contours
        # boundary filtered means contours that are complete or
        # nuclei those do not touch boundary
        bdryFiltered_labels_IDs = np.zeros((self.n_closedcontours,1))  
        bdryFiltered_area = np.zeros((self.n_closedcontours,1))

        # create new labels for closed contours only
        bdryFiltered_labels = np.zeros_like(self.image['labels'],dtype=np.uint8)
        areaFiltered_labels = np.zeros_like(self.image['labels'],dtype=np.uint8)

        true_nuclei_index = [] # store the true cells index in a list

        for i,closedcontour in enumerate(self.closedcontours):
            mask = self.image['labels'] == closedcontour+1
            bdryFiltered_labels[mask] = closedcontour+1

            bdryFiltered_labels_IDs[i] = closedcontour
            bdryFiltered_area[i] = len(np.where(mask==True)[0]) # area in terms of pixel

            area_in_um2 = bdryFiltered_area[i]*a_pixel_area
            
            if (area_in_um2 > area_threshold[0]) & (area_in_um2 < area_threshold[1]):
                # fill the values in the empty array
                areaFiltered_labels[mask] = closedcontour+1

                # append the current cell in the true_cell index
                true_nuclei_index.append(i)

        area_n_bdry_filtered_area = bdryFiltered_area[true_nuclei_index]
        self.n_true_nucleus = len(true_nuclei_index)
        self.true_nucleus = bdryFiltered_labels_IDs[true_nuclei_index]
        self.seg = {
            'area_n_bdry_filtered_IDs': bdryFiltered_labels_IDs[true_nuclei_index],
            'area_n_bdry_filtered_area': area_n_bdry_filtered_area,
            'area_n_bdry_filtered_area_in_um2': area_n_bdry_filtered_area*a_pixel_area
        }

        self.image['boundary_filtered_labels'] = bdryFiltered_labels
        self.image['area_filtered_labels'] = areaFiltered_labels
        return 

    def get_cell_info(
            self,
            probe_names:list[str]=["PolII"],
            a_pixel_area:float=0.01,
            area_threshold:list=[80,200],
            return_results:bool=False):
        """Adds `area_n_ADU` attribute that contains background subtracted
        mean intensity and the area of each nucleus and another attrubute
        `backgrounADU` which contains mean background ADU count per pixel.

        Parameters
        ----------
        probe_names : list, optional
            List of string containing name of probes, by default ["PolII"]
        a_pixel_area : float, optional
            Physical area of a pixel in um^2, by default 0.01 um^2. If 
            pixel size is other than 0.1 um, adjust this parameter 
            accordingly.
        area_threshold: list, optional
            List containing the minimum and maximum area in um^2 that each 
            nucleus can have. Default area_min is 80 um^2 and area_max is 
            200 um^2
        return_results : bool, optional
            Whether to through the result in output, by default False

        Returns
        -------
        np.ndarray
            First column is area and second and third columns ared added
            for each nuclei to store mean ADU count per pixel.
        """
        # remove boundary nucleus and filter nucleus by size 
        ReferenceImage.filter_by_boundary_n_area(self,
                                                 a_pixel_area=a_pixel_area,
                                                 area_threshold=area_threshold)
        
        # get the mask for background if not done previously 
        if not hasattr(self,"background_mask"):
            ReferenceImage.get_background_mask(self)
        
        # Store mean intensity per pixel per nucleus
        ADU_counts = np.zeros(
            (len(self.seg['area_n_bdry_filtered_IDs']),len(probe_names)))  

        for i, label in enumerate(self.seg['area_n_bdry_filtered_IDs']):
            mask = self.image['labels'] == label+1
            for j,probe in enumerate(probe_names):
                # mean intensity per pixel
                ADU_counts[i,j] = np.sum(
                    self.image[probe][mask])/self.seg['area_n_bdry_filtered_area'][i]
            
        # measure the mean background intensity and subtract it
        backgroun_area_in_pxl = len(np.where(self.background_mask==True)[0])
        mean_bg_allprobes = []
        for j,probe in enumerate(probe_names):
            mean_backgorund = np.sum(
                self.image[probe][self.background_mask])/backgroun_area_in_pxl
            
            # appen this value to a list
            mean_bg_allprobes.append(mean_backgorund)

            # subtract the background from cell intensities
            ADU_counts[:,j] = ADU_counts[:,j] - mean_backgorund

        # store values inplace
        self.ADU_counts = ADU_counts
        self.backgrounADU = mean_bg_allprobes

        if return_results:
            return self.ADU_counts
        else:
            return
        

    def get_background_mask(self,return_result=False):
        """Returns label_image for background. 

        Parameters
        ----------
        return_result : bool, optional
            Whether to return results, by default False

        Returns
        -------
        tuple
            (background_label_image, background_mask)
        """
        background = np.zeros_like(self.image['labels'],dtype=np.bool)
        bg_mask = self.image['labels'] == 0
        background[bg_mask] = 1
        self.image['background_label'] = background
        self.background_mask = bg_mask
        
        if return_result:
            return self.image['background_label'], self.background_mask

    def __repr__(self):
        return f'ReferenceImage({self.field_of_view})'
        # return f'ReferenceImage(root_path={self.root_path},\n\
    #         file_path={self.file_path},\n\
    #         field_of_view={self.field_of_view},\n\
    #         probe1_name={self.probe1_name},\n\
    #         probe2_name={self.probe2_name},\n\
    #         transmitted_name={self.transmitted_name},\n\
    #         metadata={self.metadata})'
