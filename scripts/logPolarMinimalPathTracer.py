from falcor import *

def render_graph_logPolarMinimalPathTracer():
    g = RenderGraph("logPolarMinimalPathTracer")
    AccumulatePass = createPass("AccumulatePass", {'enabled': True, 'precisionMode': 'Single'})
    g.addPass(AccumulatePass, "AccumulatePass")
    ToneMapper = createPass("ToneMapper", {'autoExposure': False, 'exposureCompensation': 0.0})
    g.addPass(ToneMapper, "ToneMapper")
    logPolarMinimalPathTracer = createPass("logPolarMinimalPathTracer", {'maxBounces': 3})
    g.addPass(logPolarMinimalPathTracer, "logPolarMinimalPathTracer")
    VBufferRT = createPass("VBufferRT", {'samplePattern': 'Stratified', 'sampleCount': 16})
    g.addPass(VBufferRT, "VBufferRT")
    g.addEdge("AccumulatePass.output", "ToneMapper.src")
    g.addEdge("VBufferRT.vbuffer", "logPolarMinimalPathTracer.vbuffer")
    g.addEdge("VBufferRT.viewW", "logPolarMinimalPathTracer.viewW")
    g.addEdge("logPolarMinimalPathTracer.color", "AccumulatePass.input")
    g.markOutput("ToneMapper.dst")
    return g

logPolarMinimalPathTracer = render_graph_logPolarMinimalPathTracer()
try: m.addGraph(logPolarMinimalPathTracer)
except NameError: None
