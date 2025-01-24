from schemes.knot import KnowledgeableNetworkofThought

def setup_scheme(args, task_loader):
    return KnowledgeableNetworkofThought(args, task_loader)
