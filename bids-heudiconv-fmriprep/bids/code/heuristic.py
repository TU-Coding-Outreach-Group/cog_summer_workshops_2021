import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    t1 = create_key('sub-{subject}/anat/sub-{subject}_T1w')
    fmap_phase = create_key('sub-{subject}/fmap/sub-{subject}_phasediff')
    fmap_mag = create_key('sub-{subject}/fmap/sub-{subject}_magnitude')
    DE_mix = create_key('sub-{subject}/func/sub-{subject}_task-DMTask_run-{item:01d}_bold')
    # canonical = ???

    info = {t1: [], fmap_phase: [], fmap_mag: [], DE_mix: []}

    #last_run = len(seqinfo)

    for s in seqinfo:
        """
        The namedtuple `s` contains the following fields:

        * total_files_till_now
        * example_dcm_file
        * series_id
        * dcm_dir_name
        * unspecified2
        * unspecified3
        * dim1
        * dim2
        * dim3
        * dim4
        * TR
        * TE
        * protocol_name
        * is_motion_corrected
        * is_derived
        * patient_id
        * study_description
        * referring_physician_name
        * series_description
        * image_type
        """

        if 't1' in s.series_description:
            info[t1] = [s.series_id]
        if (s.dim3==35) and (s.dim4==1) and ('gre_field_mapping' in s.series_description):
            info[fmap_phase].append(s.series_id)
        if (s.dim3==70) and (s.dim4==1) and ('gre_field_mapping' in s.series_description):
            info[fmap_mag].append(s.series_id)
        if (s.dim4>=233) and ('DMTask' in s.series_description):
            info[DE_mix].append(s.series_id)
            
    return info
