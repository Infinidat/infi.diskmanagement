
Count = Cint(Wscript.Arguments(0))
Subtree = Cint(Wscript.Arguments(1))
ReadAll = Cint(Wscript.Arguments(2))

Set objWMIService = GetObject("winmgmts:root\wmi")

For Counter=0 to Count:
    Set Query = objWMIService.ExecQuery("SELECT * FROM MPIO_GET_DESCRIPTOR")
    For Each Item In Query
        If Subtree=1 Then
            For Each SubItem in Item.PdoInformation
                If ReadAll=1 Then
                    None = SubItem.PathIdentifier
                    None = SubItem.DeviceState
                    None = SubItem.ScsiAddress.Lun
                    None = SubItem.ScsiAddress.PortNumber
                    None = SubItem.ScsiAddress.ScsiPathId
                    None = SubItem.ScsiAddress.TargetId
                End If
            Next
        End If
        If ReadAll=1 Then
            None = Item.InstanceName
            None = Item.DeviceName
        End If
    Next
    
    Set Query = objWMIService.ExecQuery("SELECT * FROM DSM_QueryLBPolicy_V2")
    For Each Item In Query 
        If SubTree=1 Then
            For Each SubItem in Item.LoadBalancePolicy.DSM_Paths
                If ReadAll=1 Then
                    None = SubItem.DsmPathId
                    None = SubItem.PreferredPath
                    None = Subitem.FailedPath
                    None = Subitem.OptimizedPath
                    None = Subitem.PreferredPath
                    None = Subitem.PrimaryPath
                    None = Subitem.SymmetricLUA
                    None = Subitem.TargetPort_Identifier
                    None = Subitem.TargetPortGroup_Identifier
                    None = Subitem.TargetPortGroup_Preferred
                    None = Subitem.TargetPortGroup_State
                End If
            Next
        End If
        If ReadAll=1 Then
            None = Item.InstanceName
            None = Item.LoadBalancePolicy.LoadBalancePolicy
        End If
    Next
Next
