#!/usr/bin/env python3
"""
This is a script for a custom bookkeeping job. Its job is to write a script
into an evaluation directory that will perform further analysis on the node.
This can also be run on existing evaluation nodes to analyze them as needed.
"""
import scriptconfig as scfg
import ubelt as ub


class WriteAnalysisConfig(scfg.DataConfig):
    eval_dpath = scfg.Value(None, help='the path to the evaluation node')


def build_analysis_script():
    template = ub.codeblock(
        '''

        ''')



def main(cmdline=1, **kwargs):
    """
    Example:
        >>> # xdoctest: +SKIP
        >>> cmdline = 0
        >>> kwargs = dict()
        >>> main(cmdline=cmdline, **kwargs)
    """
    import rich
    config = WriteAnalysisConfig.cli(cmdline=cmdline, data=kwargs, strict=True)
    rich.print('config = ' + ub.urepr(config, nl=1))

if __name__ == '__main__':
    """

    CommandLine:
        python ~/code/watch/watch/mlops/write_analysis_script.py
        python -m watch.mlops.write_analysis_script
    """
    main()
